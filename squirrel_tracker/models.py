from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    Latitude = models.FloatField('X', blank=False)
    Longitude = models.FloatField('Y', blank=False)
    UniqueSquirrelID = models.CharField(primary_key=True, max_length=255, blank=False)
    Hectare = models.CharField('Hectare', max_length=255, blank=True)
    Shift = models.CharField('Shift', max_length=255, blank=True)
    Date = models.CharField('Date', max_length=255, blank=True)
    HectareSquirrelNumber = models.IntegerField('HectareSquirrelNumber', blank=True)
    Age = models.CharField('Age', max_length=255, blank=True)
    PrimaryFurColor = models.CharField('PrimaryFurColor', max_length=255, blank=True)
    HighlightFurColor = models.CharField('HighlightFurColor', max_length=255, blank=True)
    CombinationOfPrimaryAndHighlightColor = models.CharField('CombinationOfPrimaryAndHighlightColor', max_length=255, blank=True)
    ColorNotes = models.CharField('ColorNotes', max_length=255, blank=True)
    Location = models.CharField('Location', max_length=255, blank=True)
    AboveGroundSighterMeasurement = models.CharField('AboveGroundSighterMeasurement', max_length=255, blank=True)
    SpecificLocation = models.CharField('SpecificLocation', max_length=255, blank=True)
    Running = models.BooleanField('Running', blank=True)
    Chasing = models.BooleanField('Chasing', blank=True)
    Climbing = models.BooleanField('Climbing', blank=True)
    Eating = models.BooleanField('Eating', blank=True)
    Foraging = models.BooleanField('Foraging', blank=True)
    OtherActivities = models.CharField('OtherActivities', max_length=255, blank=True)
    Kuks = models.BooleanField('Kuks', blank=True)
    Quaas = models.BooleanField('Quaas', blank=True)
    Moans = models.BooleanField('Moans', blank=True)
    TailFlags = models.BooleanField('TailFlags', blank=True)
    TailTwitches = models.BooleanField('TailTwitches', blank=True)
    Approaches = models.BooleanField('Approaches', blank=True)
    Indifferent = models.BooleanField('Indifferent', blank=True)
    RunsFrom = models.BooleanField('RunsFrom', blank=True)
    OtherInteractions = models.CharField('OtherInteractions', max_length=255, blank=True)
    LatLong = models.CharField('Latlong', max_length=255, blank=True)

    def __str__(self):
        return f'Suirrel ID: {self.UniqueSquirrelID}'
