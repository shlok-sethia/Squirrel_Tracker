from django.core.management.base import BaseCommand, CommandError
from dateutil import parser
from squirrel_tracker.models import Squirrel
import csv


class Command(BaseCommand):
    help = 'transfers data from table to csv file'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Squirrel

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')
