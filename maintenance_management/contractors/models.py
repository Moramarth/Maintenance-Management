from django.contrib.auth import get_user_model
from django.db import models

from maintenance_management.supervisor.models import Assignments

UserModel = get_user_model()


class Meeting(models.Model):
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    assignment = models.ForeignKey(
        Assignments,
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
    )
