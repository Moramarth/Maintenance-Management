from django.db import models


class Company(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )

    business_field = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )

    additional_information = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    company_logo = models.ImageField(
        blank=True,
        null=True,
    )
