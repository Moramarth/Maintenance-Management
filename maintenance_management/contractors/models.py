from django.contrib.auth import get_user_model
from django.db import models

from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


class Meeting(models.Model):
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )
    meeting_date = models.DateTimeField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"Meeting created by {self.created_by}"


class ExpensesEstimate(models.Model):
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )
    additional_information = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )
    attached_file = models.FileField(
        upload_to="documents",
        blank=True,
        null=True,
        validators=[validate_file_size],
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title} created by {self.created_by}"
