# people/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("list_people/", views.list_people),
]
