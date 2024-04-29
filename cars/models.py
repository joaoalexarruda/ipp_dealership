from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    body_type = models.CharField(max_length=200)
    power = models.IntegerField(blank=True, null=True)
    cylinder_number = models.IntegerField(blank=True, null=True)
    fuel = models.CharField(max_length=200)
    gearbox = models.CharField(max_length=200)
    doors = models.IntegerField(blank=True, null=True)
    quilometers = models.IntegerField(blank=True, null=True)
    def __str__(self): 
        return self.model
