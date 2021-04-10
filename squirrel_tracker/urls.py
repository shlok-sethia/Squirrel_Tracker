from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<squirrel_id>', views.update_location, name='update'),
    path('sightings/add', views.add_sighting(), name='add')
]
