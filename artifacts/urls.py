# people/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"artifacts", views.ArtifactViewSet, "artifact")

urlpatterns = [
    path("", include(router.urls)),
]
