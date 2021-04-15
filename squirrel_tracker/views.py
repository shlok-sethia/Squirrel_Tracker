from django.shortcuts import render, redirect
from squirrel_tracker.models import Squirrel
from squirrel_tracker.forms import SquirrelForm
from squirrel_tracker.forms import AddSquirrelForm


def index(request):
    return render(request, 'squirrel_tracker/index.html',{})

def map_squirrels(request):
    squirrel_data = Squirrel.objects.all()[:100]
    return render(request, 'squirrel_tracker/map.html', {'squ': squirrel_data})

def sightings(request):
    squirrel_data = Squirrel.objects.all()
    return render(request, 'squirrel_tracker/sightings.html', {'squ': squirrel_data})

def update_squirrel(request, squirrel_id):
    squirrel_data = Squirrel.objects.get(UniqueSquirrelID=squirrel_id)
    if request.method == 'POST':
        print('yes')
        form_data = SquirrelForm(request.POST, instance=squirrel_data)
        if form_data.is_valid():
            form_data.save()
            return redirect(f'/squirrel_tracker/sightings/{squirrel_id}')
    else:
        form_data = SquirrelForm(instance=squirrel_data)
    return render(request, 'squirrel_tracker/update.html', {'form_data': form_data})

def add_sighting(request):
    if request.method == 'POST':
        form_data = AddSquirrelForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    else:
        form_data = AddSquirrelForm()
    return render(request, 'squirrel_tracker/add.html', {"form_data": form_data})

def get_stats(request):
    color_count = dict()
    primary_fur_colors = Squirrel.objects.values('PrimaryFurColor').distinct()
    for color in primary_fur_colors:
        if color['PrimaryFurColor'] == '' or color['PrimaryFurColor'] is None:
            continue
        else:
            color_count[color['PrimaryFurColor']]=len(Squirrel.objects.filter(PrimaryFurColor=color['PrimaryFurColor']))
    print(color_count)

    activities = dict()
    running = Squirrel.objects.filter(Running=True)
    activities['running']=len(running)
    chasing = Squirrel.objects.filter(Chasing=True)
    activities['chasing']=len(chasing)
    climbing = Squirrel.objects.filter(Climbing=True)
    activities['climbing']=len(climbing)
    eating = Squirrel.objects.filter(Eating=True)
    activities['eating']=len(eating)
    foraging = Squirrel.objects.filter(Foraging=True)
    activities['foraging']=len(foraging)

    alarms = dict()
    alarms['Kuks'] = len(Squirrel.objects.filter(Kuks=True))
    alarms['Quaas'] = len(Squirrel.objects.filter(Quaas=True))
    alarms['Moans'] = len(Squirrel.objects.filter(Moans=True))
    alarms['TailFlags'] = len(Squirrel.objects.filter(TailFlags=True))
    alarms['TailTwitches'] = len(Squirrel.objects.filter(TailTwitches=True))
    alarms['Approaches'] = len(Squirrel.objects.filter(Approaches=True))
    alarms['Indifferent'] = len(Squirrel.objects.filter(Indifferent=True))
    alarms['RunsFrom'] = len(Squirrel.objects.filter(RunsFrom=True))

    ages = dict()
    age_groups = Squirrel.objects.values('Age').distinct()
    for age in age_groups:
        if age['Age'] == '' or age['Age']=='?':
            continue
        else:
            ages[age['Age']] = len(Squirrel.objects.filter(Age=age['Age']))

    return render(request, 'squirrel_tracker/stats.html', {
        'fur_color': color_count,'activities': activities,
        'alarms':alarms, 'ages':ages})
