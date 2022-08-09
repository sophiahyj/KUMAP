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
    return 'static/image/{}/{}'.format(building_name, filename)

class Entrance(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    entrance_name = models.CharField(max_length=50)
    entrance_time1 = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    entrance_time2 = models.TextField(null=True)
    entrance_lat = models.FloatField(default=0.0)   
    entrance_lon = models.FloatField(default=0.0)
    entrance_num = models.IntegerField(null=True)
    # entrance_photo = models.ImageField(null=True, upload_to="static/image/{id}".format(id = building_id), blank=True)
    entrance_photo = models.ImageField(null=True, upload_to=directory, blank=True)

    
    def __str__(self):
        return self.building_id.building_name

FACILITY_CHOICES = (
        ('cafe', '카페'),
        ('restaurant', '식당'),
        ('one-stop', '원스톱'),
        ('book_return', '책반납기'),
        ('printer', '프린터'),
        ('lounge', '스터디'),
    )

class Facility(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)


    category = models.CharField(max_length=20, choices=FACILITY_CHOICES)
    facility_name = models.CharField(max_length=50)
    facility_loc = models.TextField(null=True)

    def __str__(self):
        return self.facility_name