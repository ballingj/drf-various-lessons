# vehicles/serializers/vehicles.py
from rest_framework import serializers
from vehicles.models import Vehicle, Part


# Custom serializer to assemble a serial_no from part's make and id field
class SerialNumberField(serializers.Field):
    def to_representation(self, value):
        code = value.make[:3].upper()
        return f"{code}-{value.id}"


class PartSerializer(serializers.ModelSerializer):
    serial_no = SerialNumberField(source="*")

    class Meta:
        model = Part
        fields = ["url", "name", "vehicle", "serial_no"]


# example of object pulling data from another serializer -- PartSerializer
# One vehicle will have multiple parts - to be shown in part_set field
class VehicleSerializer(serializers.ModelSerializer):
    part_set = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ["url", "name", "part_set"]
