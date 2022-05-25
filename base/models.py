from django.db import models

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100, unique=True)
    #place_city = models.CharField(max_length=100)
    #place_country = models.CharField(max_length=100)
    #place_zip = models.CharField(max_length=100)
    place_address = models.CharField(max_length=100) # street address

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, unique=True)
    event_description = models.CharField(max_length=100)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_place = models.ForeignKey(Place, on_delete=models.CASCADE)