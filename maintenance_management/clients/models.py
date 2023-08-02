from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from maintenance_management.accounts.validators import validate_file_size
from maintenance_management.common.models import Company

UserModel = get_user_model()


class ServiceReport(models.Model):
    MAX_LENGTH_FOR_TITLE = 50
    MAX_LENGTH_FOR_DESCRIPTION = 500
    MAX_LENGTH_FOR_REPORT_STATUS = 8
    MAX_LENGTH_FOR_REPORT_TYPE = 20

    class ReportStatus(models.TextChoices):
        PENDING = "Pending"
        ASSIGNED = "Assigned"
        DONE = "Done"
        REJECTED = "Rejected"

    class ReportType(models.TextChoices):
        NETWORKING = "Networking"
        ELECTRICAL = "Electrical"
        PLUMBING = "Plumbing"
        STRUCTURAL_INTEGRITY = "Structural Integrity"
        SECURITY_SYSTEMS = "Security Systems"
        LANDSCAPING = "Landscaping"
        OTHER = "Other"

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=MAX_LENGTH_FOR_TITLE,
        blank=False,
        null=False,
    )
    description = models.TextField(
        max_length=MAX_LENGTH_FOR_DESCRIPTION,
        blank=False,
        null=False,
    )
    file = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        validators=[validate_file_size],
        verbose_name="Image",
    )
    report_status = models.CharField(
        max_length=MAX_LENGTH_FOR_REPORT_STATUS,
        blank=False,
        choices=ReportStatus.choices,
        default=ReportStatus.PENDING,
    )
    assigned_to = models.ForeignKey(
        UserModel,
        related_name="assigned_to",
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True,
    )
    submit_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    report_type = models.CharField(
        max_length=MAX_LENGTH_FOR_REPORT_TYPE,
        blank=False,
        choices=ReportType.choices,
        default=ReportType.OTHER,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('report details', args=[self.pk])


class Review(models.Model):
    MAX_LENGTH_FOR_COMMENT = 500

    class Rating(models.IntegerChoices):
        ONE = 1, "Very Bad"
        TWO = 2, "Bad"
        THREE = 3, "Good"
        FOUR = 4, "Very good"
        FIVE = 5, "Excellent"

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    service_report = models.ForeignKey(
        ServiceReport,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    rating = models.PositiveIntegerField(
        blank=False,
        null=False,
        choices=Rating.choices
    )
    comment = models.TextField(
        max_length=MAX_LENGTH_FOR_COMMENT,
        blank=True,
        null=True,
    )
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating} Comment: {self.comment}"
