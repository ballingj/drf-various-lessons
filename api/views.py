# api/views.py
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from artifacts.models import Artifact
from people.models import Person
from vehicles.models import Vehicle
from people.serializers import PersonSerializer
from vehicles.serializers.vehicles import VehicleSerializer


@api_view(["GET"])
def listing(request):
    doctors = Person.objects.filter(title="Dr.")
    vehicles = Vehicle.objects.all()

    '''You may recall that the VehicleSerializer uses the url field. In order to
    properly populate the url field, the serializer needs to be aware of the request.
    When you use a ViewSet, the ViewSet does this automatically for you. Because I’m not
    using a ViewSet here, I need to pass extra information into the VehicleSerializer so 
    that it can see the request object. This is done through the context parameter.'''
    
    context = {
        "request": request,
    }
    vehicle_serializer = VehicleSerializer(vehicles, many=True, context=context)

    results = {
        "doctors": PersonSerializer(doctors, many=True).data,
        "vehicles": vehicle_serializer.data,
    }

    return Response(results)


class DoctorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request):
        doctors = Person.objects.filter(title="Dr.")
        results = {
            "doctors": PersonSerializer(doctors, many=True).data,
        }

        return Response(results)


class MassDeleteArtifactsViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    @action(detail=False, methods=["delete"])
    def mass_delete(self, request, pk=None):
        for artifact_id in request.POST["ids"].split(","):
            Artifact.objects.get(id=artifact_id).delete()

        return Response()
