# vehicle/views/vehicles.py
from rest_framework import viewsets
from rest_framework.response import Response

from vehicles.models import Vehicle, Part
from vehicles.serializers.vehicles import VehicleSerializer, PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.all()
