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

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        columns = Squirrel._meta.fields
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for i in Squirrel.objects.all():
                row = [getattr(i, col.name) for col in columns]
                writer.writerow(row)
            f.close()
