from django.contrib.auth import get_user_model
from django.db import models

from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.contractors.validators import meeting_is_in_the_future_validator
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


class Meeting(models.Model):
    MAX_LENGTH_FOR_DESCRIPTION = 500

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        max_length=MAX_LENGTH_FOR_DESCRIPTION,
        blank=False,
        null=False,
    )
    meeting_date = models.DateTimeField(
        blank=False,
        null=False,
        validators=[meeting_is_in_the_future_validator]
    )

    def __str__(self):
        return f"Meeting created by {self.created_by}"


class ExpensesEstimate(models.Model):
    MAX_LENGTH_FOR_TITLE = 150
    MAX_LENGTH_FOR_ADDITIONAL_INFORMATION = 500

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=MAX_LENGTH_FOR_TITLE,
        blank=False,
        null=False,
    )
    additional_information = models.TextField(
        max_length=MAX_LENGTH_FOR_ADDITIONAL_INFORMATION,
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
