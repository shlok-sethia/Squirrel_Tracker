from django.shortcuts import render


def index(request):
    return render(request, 'squirrel_tracker/index.html',{})


def map(request):
    return render(request, 'squirrel_tracker/map.html')
