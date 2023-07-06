from django.db import models

from maintenance_management.accounts.models import AbstractProfile


class EngineeringProfile(AbstractProfile):
    EXPERTISE_CHOICES = (
        ("Networking", "Networking"),
        ("Electrical", "Electrical"),
        ("Plumbing", "Plumbing"),
        ("Structural Integrity", "Structural Integrity"),
        ("Security Systems", "Security Systems"),
        ("Landscaping", "Landscaping"),
    )

    expertise = models.CharField(max_length=50, choices=EXPERTISE_CHOICES)
