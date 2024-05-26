# artifacts/admin.py
from django.contrib import admin

from .models import Artifact


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "shiny",
    )
