from django.db import models
from django.urls import reverse

from maintenance_management.accounts.validators import validate_file_size


class Company(models.Model):
    MAX_LENGTH_FOR_NAME = 150
    MAX_LENGTH_FOR_BUSINESS_FIELD = 250
    MAX_LENGTH_FOR_ADDITIONAL_INFORMATION = 500

    name = models.CharField(
        max_length=MAX_LENGTH_FOR_NAME,
        blank=False,
        null=False,
    )

    business_field = models.CharField(
        max_length=MAX_LENGTH_FOR_BUSINESS_FIELD,
        blank=True,
        null=True,
    )

    additional_information = models.TextField(
        max_length=MAX_LENGTH_FOR_ADDITIONAL_INFORMATION,
        blank=True,
        null=True,
    )

    company_logo = models.ImageField(
        blank=True,
        null=True,
        upload_to="images",
        validators=[validate_file_size]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('company details', args=[self.pk])

    def __str__(self):
        return f"{self.name} - Business Field: {self.business_field or 'Not shown'}"

    class Meta:
        verbose_name_plural = "Companies"
