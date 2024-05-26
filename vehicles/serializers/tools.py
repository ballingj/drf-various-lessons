# vehicles/serializers/tools.py
from rest_framework import serializers

class ToolSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    make = serializers.CharField(max_length=50)
