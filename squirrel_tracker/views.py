from django.shortcuts import render
from squirrel_tracker.models import Squirrel
from squirrel_tracker.forms import SquirrelForm

def index(request):
    return render(request, 'squirrel_tracker/index.html',{})

def map(request):
    squirrel_data = Squirrel.objects.all()[:100]
    return render(request, 'squirrel_tracker/map.html', {'squ': squirrel_data})

def sightings(request):
    return render(request, 'squirrel_tracker/sightings.html', {})

def update_squirrel(request, squirrel_id):
    squirrel_data = Squirrel.objects.get(UniqueSquirrelID=squirrel_id)
    form_data = SquirrelForm(instance=squirrel_data)
    return render(request, 'squirrel_tracker/update.html', {'form_data': form_data})

def add_sighting(request):
    return render(request, 'squirrel_tracker/add.html', {})

def get_stats(request):
    return render(request, 'squirrel_tracker/stats.html', {})
