from django.db import models

from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.common.models import Company
from maintenance_management.estate.validators import city_name_validation


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
        validators=[city_name_validation]
    )
    address = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    picture = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        validators=[validate_file_size]
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
