# vehicles/models/vehicles.py
from django.db import models


# example of tables/object with foreign key.  one Vehicle : many Parts
# See serializer file how to serialize these -- VehicleSerializer & PartSerializer
# One vehicle will have multiple parts - to be shown in part_set field
class Vehicle(models.Model):
    name = models.CharField(max_length=100)


class Part(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
