from django.shortcuts import render
from .models import Antenna

def antenna_map(request):
    antennas = Antenna.objects.all()
    return render(request, 'antenna_map/antenna_map.html', {'antennas': antennas})
