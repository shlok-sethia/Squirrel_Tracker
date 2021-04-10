from django.shortcuts import render
from squirrel_tracker.models import Squirrel

def index(request):
    return render(request, 'squirrel_tracker/index.html',{})


def map(request):
    squirrel_data = Squirrel.objects.all()[:100]
    return render(request, 'squirrel_tracker/map.html', {'squ': squirrel_data})

def sightings(request):
    return render(request, 'squirrel_tracker/sightings.html', {})

def update_location(request, squirrel_id):
    return render(request, 'squirrel_tracker/update.html', {})

def add_sighting(request):
    return render(request, 'squirrel_tracker/add.html', {})
