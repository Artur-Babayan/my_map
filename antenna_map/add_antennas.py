import csv
from antenna_map.models import Antenna

with open('antenna_map_antenna_202304121658.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        my_model = Antenna(
            name=row['name'],
            configuration=row['configuration'],
            latitude=row['latitude'],
            longitude=row['longitude']
        )
        my_model.save()
