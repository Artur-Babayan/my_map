from django.urls import path
from django.core.management import call_command
from antenna_map.views import antenna_map

urlpatterns = [
    path('', antenna_map, name='antenna_map'),
    path('import-antennas/', lambda request: call_command('import_antennas', 'path/to/your/csvfile.csv'), name='import_antennas'),

]
