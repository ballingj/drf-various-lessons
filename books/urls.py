# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"books", views.BookViewSet, "book")

urlpatterns = [
    path("", include(router.urls)),
    path("library/", views.library),
]
