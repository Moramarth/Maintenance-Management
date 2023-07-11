from django.db import models

from maintenance_management.accounts.models import AppUser
from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.common.models import Company


class ServiceReport(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    description = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )
    image = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        validators=[validate_file_size],
    )
    report_status = models.CharField(
        max_length=50,
        blank=False,
        default="Pending",
    )
    submit_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

# TODO: create Review model
