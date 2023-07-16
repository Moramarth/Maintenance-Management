from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from maintenance_management.clients.models import ServiceReport

UserModel = get_user_model()


class Assignment(models.Model):
    class AssignmentStatus(models.TextChoices):
        PENDING = "Pending"
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"

    service_report = models.ForeignKey(
        ServiceReport,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    # Engineer or Contractor that was given the assignment
    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    meeting_required = models.BooleanField(blank=True)
    expense_estimate_available = models.BooleanField(blank=True)
    date_assigned = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    assigned_by = models.ForeignKey(
        UserModel,
        related_name="contact_information",
        on_delete=models.SET_NULL,
        null=True,
    )
    assignment_status = models.CharField(
        max_length=8,
        blank=False,
        choices=AssignmentStatus.choices,
        default=AssignmentStatus.PENDING,
    )

    def get_absolute_url(self):
        return reverse('assignment details', args=[self.pk])

    def __str__(self):
        return f"'{self.service_report}' assigned to {self.user}"
