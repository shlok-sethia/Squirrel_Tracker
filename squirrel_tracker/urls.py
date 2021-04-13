from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map_squirrels, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    re_path('sightings/([\w]*-[\w]*-[\w]*-[\w]*)', views.update_squirrel, name='update'),
    path('sightings/add', views.add_sighting, name='add'),
    path('sightings/stats', views.get_stats, name='stats')
]
