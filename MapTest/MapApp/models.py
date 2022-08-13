from distutils.command.build import build
from fileinput import filename
from django.db import models

# Create your models here.
class Building(models.Model):
    building_name = models.CharField(max_length=50)
    history = models.TextField(null=True)
    building_lat =  models.FloatField(default=0.0)
    building_lon = models.FloatField(default=0.0)

    def __str__(self):
        return self.building_name

def directory(building_name, filename):
    return 'user_{}/{}'.format(building_name, filename)

class Entrance(models.Model):
    building_id = models.ForeignKey('Building', on_delete=models.CASCADE)


    entrance_name = models.CharField(max_length=50)
    entrance_time1 = models.TimeField(auto_now=False, auto_now_add=False)
    entrance_time2 = models.TextField()
    entrance_lat = models.FloatField(default=0.0)   
    entrance_lon = models.FloatField(default=0.0)
  

    
    def __str__(self):
        return self.entrance_name

FACILITY_CHOICES = (
        ('cafe', 'cafe'),
        ('restaurant', 'restaurant'),
        ('one-stop', 'one-stop'),
        ('book_return', 'book_return'),
        ('printer', 'printer'),
        ('lounge', 'lounge'),
    )

class Facility(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=FACILITY_CHOICES)
    facility_name = models.CharField(max_length=50)
    facility_loc = models.TextField()

    def __str__(self):
        return self.facility_name