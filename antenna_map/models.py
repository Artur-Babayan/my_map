from django.db import models

class Antenna(models.Model):
    name = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name
