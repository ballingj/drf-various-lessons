# people/models.py
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    title = models.CharField(max_length=5)

    class Meta:
        # Define the special plural name for person
        verbose_name_plural = "People"
