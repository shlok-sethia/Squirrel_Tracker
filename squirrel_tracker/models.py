from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Squirrel(models.Model):
    X = models.FloatField('X')
    Y = models.FloatField('Y')
    UniqueSquirrelID = models.CharField(primary_key=True, max_length=255)
    Hectare = models.CharField('Hectare', max_length=255)
    Shift = models.CharField('Shift', max_length=255)
    Date = models.DateField('Date')
    HectareSquirrelNumber = models.IntegerField('HectareSquirrelNumber')
    Age = models.CharField('Age', max_length=255)
    PrimaryFurColor = models.CharField('PrimaryFurColor', max_length=255)
    HighlightFurColor = models.CharField('HighlightFurColor', max_length=255)
    CombinationOfPrimaryAndHighlightColor = models.CharField('CombinationOfPrimaryAndHighlightColor', max_length=255)
    ColorNotes = models.CharField('ColorNotes', max_length=255)
    Location = models.CharField('Location', max_length=255)
    AboveGroundSighterMeasurement = models.CharField('AboveGroundSighterMeasurement', max_length=255)
    SpecificLocation = models.CharField('SpecificLocation', max_length=255)
    Running = models.BooleanField('Running')
    Chasing = models.BooleanField('Chasing')
    Climbing = models.BooleanField('Climbing')
    Eating = models.BooleanField('Eating')
    Foraging = models.BooleanField('Foraging')
    OtherActivities = models.CharField('OtherActivities', max_length=255)
    Kuks = models.BooleanField('Kuks')
    Quaas = models.BooleanField('Quaas')
    Moans = models.BooleanField('Moans')
    TailFlags = models.BooleanField('TailFlags')
    TailTwitches = models.BooleanField('TailTwitches')
    Approaches = models.BooleanField('Approaches')
    Indifferent = models.BooleanField('Indifferent')
    RunsFrom = models.BooleanField('RunsFrom')
    OtherInteractions = models.CharField('OtherInteractions', max_length=255)
    LatLong = models.CharField('Latlong', max_length=255)

    def __str__(self):
        return f'Suirrel ID: {self.UniqueSquirrelID}'


