from rest_framework import viewsets

from .models import Artifact
from .serializers import ArtifactSerializer


class ArtifactViewSet(viewsets.ModelViewSet):
    serializer_class = ArtifactSerializer
    
    def get_queryset(self):
        return Artifact.objects.all()
