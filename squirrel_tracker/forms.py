from django.forms import ModelForm
from .models import Squirrel


class SquirrelForm(ModelForm):
	class Meta:
		model = Squirrel
		fields = ['Latitude', 'Longitude', 'UniqueSquirrelID', 'Shift', 'Date', 'Age']


class AddSquirrelForm(ModelForm):
	class Meta:
		model = Squirrel
		fields = '__all__'

