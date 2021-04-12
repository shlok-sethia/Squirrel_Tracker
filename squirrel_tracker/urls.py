from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<str:squirrel_id>', views.update_squirrel, name='update'),
    path('sightings/add', views.add_sighting, name='add'),
    path('sightings/stats', views.get_stats, name='stats')
]
