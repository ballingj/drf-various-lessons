# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"doctors", views.DoctorsViewSet, "doctor")
router.register(r"mass_delete", views.MassDeleteArtifactsViewSet, "mass_delete")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/listing/", views.listing),
]
