from django.db import models
from django.urls import reverse

from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.common.models import Company
from maintenance_management.estate.validators import city_name_validation


class Building(models.Model):
    MAX_LENGTH_FOR_NAME = 50
    MAX_LENGTH_FOR_CITY = 50
    MAX_LENGTH_FOR_ADDRESS = 200

    name = models.CharField(
        max_length=MAX_LENGTH_FOR_NAME,
        blank=False,
        null=False,
    )
    city = models.CharField(
        max_length=MAX_LENGTH_FOR_CITY,
        blank=False,
        null=False,
        validators=[city_name_validation]
    )
    address = models.CharField(
        max_length=MAX_LENGTH_FOR_ADDRESS,
        blank=False,
        null=False,
    )
    file = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        validators=[validate_file_size],
        verbose_name="Picture",
    )

    latitude = models.FloatField(
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        blank=True,
        null=True,
    )
    tenants = models.ManyToManyField(Company, through="AdditionalAddressInformation")

    def get_absolute_url(self):
        return reverse('building details', args=[self.pk])

    def __str__(self):
        return self.name


class AdditionalAddressInformation(models.Model):
    MAX_LENGTH_FOR_SECTION = 50

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    section = models.CharField(
        max_length=MAX_LENGTH_FOR_SECTION,
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

    class Meta:
        verbose_name_plural = "Additional address information"
