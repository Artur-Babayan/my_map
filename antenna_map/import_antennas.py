import csv
from django.core.management.base import BaseCommand
from antenna_map.models import Antenna


class Command(BaseCommand):
    help = 'Import antenna data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str)

    def handle(self, *args, **options):
        csvfile = options['csvfile']

        with open(csvfile, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                name = row[0]
                configuration = row[1]
                latitude = row[2]
                longitude = row[3]
                status = row[4]
                antenna = Antenna(name=name, configuration=configuration, latitude=latitude, longitude=longitude, status=status)
                antenna.save()

        self.stdout.write(self.style.SUCCESS('Antennas imported successfully.'))
