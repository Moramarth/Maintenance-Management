import uuid
from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from maintenance_management.accounts.managers import AppUserManager
from maintenance_management.common.models import Company

from .validators import only_letters_validator, PHONE_VALIDATION, validate_file_size, first_char_validation


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = "email"

    objects = AppUserManager()

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )


UserModel = get_user_model()


class AppUserProfile(models.Model):
    class FieldOfExpertise(models.TextChoices):
        NETWORKING = "Networking"
        ELECTRICAL = "Electrical"
        PLUMBING = "Plumbing"
        STRUCTURAL_INTEGRITY = "Structural Integrity"
        SECURITY_SYSTEMS = "Security Systems"
        LANDSCAPING = "Landscaping"

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=[MinLengthValidator(2), only_letters_validator, first_char_validation],
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=[MinLengthValidator(2), only_letters_validator, first_char_validation],
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[PHONE_VALIDATION]
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        validators=[validate_file_size]
    )

    expertise = models.CharField(
        max_length=20,
        blank=True,
        choices=FieldOfExpertise.choices,
        default='Not suitable',
    )

    def get_absolute_url(self):
        return reverse('profile details', args=[self.pk])


class RegisterInvitation(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
    )
    unique_identifier = models.UUIDField(default=uuid.uuid4, primary_key=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    groups = models.ForeignKey(auth_models.Group, on_delete=models.CASCADE)

    secondary_email = models.EmailField(
        blank=False,
        null=False,
        help_text=_("You will get a copy of the invitation to be sure sending was properly handled"),
        verbose_name="Your Email:"
    )
