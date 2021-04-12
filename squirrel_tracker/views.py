from django.shortcuts import render, redirect
from squirrel_tracker.models import Squirrel
from squirrel_tracker.forms import SquirrelForm
from squirrel_tracker.forms import AddSquirrelForm


def index(request):
    return render(request, 'squirrel_tracker/index.html',{})

def map(request):
    squirrel_data = Squirrel.objects.all()[:100]
    return render(request, 'squirrel_tracker/map.html', {'squ': squirrel_data})

def sightings(request):
    squirrel_data = Squirrel.objects.all()[:100]
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
    return render(request, 'squirrel_tracker/stats.html', {})
