from django.db import models

from maintenance_management.common.models import Company


class Building(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    city = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    address = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    tenants = models.ManyToManyField(Company, through="AdditionalAddressInformation")


class AdditionalAddressInformation(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    section = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    floor = models.IntegerField(
        blank=False,
        null=False,
    )
    office_number = models.PositiveIntegerField(
        blank=False,
        null=False,
    )
