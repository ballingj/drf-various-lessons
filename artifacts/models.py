from django.db import models

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    shiny = models.BooleanField()
