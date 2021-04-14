from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    Latitude = models.FloatField('X', blank=False)
    Longitude = models.FloatField('Y', blank=False)
    UniqueSquirrelID = models.CharField(primary_key=True, max_length=255, blank=False)
    Hectare = models.CharField('Hectare', max_length=255, null=True, blank=True)
    Shift = models.CharField('Shift', max_length=255, null=True, blank=True)
    Date = models.CharField('Date', max_length=255, null=True, blank=True)
    HectareSquirrelNumber = models.IntegerField('HectareSquirrelNumber', null=True, blank=True)
    Age = models.CharField('Age', max_length=255, blank=True)
    PrimaryFurColor = models.CharField('PrimaryFurColor', max_length=255, null=True, blank=True)
    HighlightFurColor = models.CharField('HighlightFurColor', max_length=255, null=True, blank=True)
    CombinationOfPrimaryAndHighlightColor = models.CharField('CombinationOfPrimaryAndHighlightColor', max_length=255, null=True, blank=True)
    ColorNotes = models.CharField('ColorNotes', max_length=255, null=True, blank=True)
    Location = models.CharField('Location', max_length=255, null=True, blank=True)
    AboveGroundSighterMeasurement = models.CharField('AboveGroundSighterMeasurement', max_length=255, null=True, blank=True)
    SpecificLocation = models.CharField('SpecificLocation', max_length=255, null=True, blank=True)
    Running = models.BooleanField('Running', null=True, blank=True)
    Chasing = models.BooleanField('Chasing', null=True, blank=True)
    Climbing = models.BooleanField('Climbing', null=True, blank=True)
    Eating = models.BooleanField('Eating', null=True, blank=True)
    Foraging = models.BooleanField('Foraging', null=True, blank=True)
    OtherActivities = models.CharField('OtherActivities', max_length=255, null=True, blank=True)
    Kuks = models.BooleanField('Kuks', null=True, blank=True)
    Quaas = models.BooleanField('Quaas', null=True, blank=True)
    Moans = models.BooleanField('Moans', null=True, blank=True)
    TailFlags = models.BooleanField('TailFlags', null=True, blank=True)
    TailTwitches = models.BooleanField('TailTwitches', null=True, blank=True)
    Approaches = models.BooleanField('Approaches', null=True, blank=True)
    Indifferent = models.BooleanField('Indifferent', null=True, blank=True)
    RunsFrom = models.BooleanField('RunsFrom', null=True, blank=True)
    OtherInteractions = models.CharField('OtherInteractions', max_length=255, null=True, blank=True)
    LatLong = models.CharField('Latlong', max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Squirrel ID: {self.UniqueSquirrelID}'
