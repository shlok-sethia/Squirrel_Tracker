from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from dateutil import parser
from datetime import datetime
from squirrel_tracker.models import Squirrel
import csv
import os
import re

class Command(BaseCommand):
    help = 'populates squirrels table'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Squirrel

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')


    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        # file_path = self.get_csv_file(filename)

        line_count = 0
        squirrel_id = list()

        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        try:
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                #self.clear_model()
                for row in csv_reader:
                    if row != '' and line_count >= 1 and row[2] not in squirrel_id:
                        m, d, y = pattern.match(row[5]).groups()
                        squirrel = Squirrel.objects.create(
                            Latitude = float(row[0]),
                            Longitude = float(row[1]),
                            UniqueSquirrelID = row[2],
                            Hectare = row[3],
                            Shift = row[4],
                            #Date = date(int(y), int(m), int(d)),
                            Date=datetime.strptime(str(row[5]), '%m%d%Y').date(),
                            HectareSquirrelNumber = int(row[6]),
                            Age = row[7],
                            PrimaryFurColor = row[8],
                            HighlightFurColor = row[9],
                            CombinationOfPrimaryAndHighlightColor = row[10],
                            ColorNotes = row[11],
                            Location = row[12],
                            AboveGroundSighterMeasurement = row[13],
                            SpecificLocation = row[14],
                            Running = True if row[15] == 'TRUE' else False,
                            Chasing = True if row[16] == 'TRUE' else False,
                            Climbing = True if row[17] == 'TRUE' else False,
                            Eating = True if row[18] == 'TRUE' else False,
                            Foraging = True if row[19] == 'TRUE' else False,
                            OtherActivities = True if row[20] == 'TRUE' else False,
                            Kuks = True if row[21] == 'TRUE' else False,
                            Quaas = True if row[22] == 'TRUE' else False,
                            Moans = True if row[23] == 'TRUE' else False,
                            TailFlags = True if row[24] == 'TRUE' else False,
                            TailTwitches = True if row[25] == 'TRUE' else False,
                            Approaches = True if row[26] == 'TRUE' else False,
                            Indifferent = True if row[27] == 'TRUE' else False,
                            RunsFrom = True if row[28] == 'TRUE' else False,
                            OtherInteractions = row[29],
                            LatLong = row[30]
                        )

                        squirrel_id.append(row[2])
                    line_count += 1

        except FileNotFoundError as fe:
            raise CommandError(f'File {filename} does not exist')
