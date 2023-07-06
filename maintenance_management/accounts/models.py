import uuid
from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from maintenance_management.accounts.managers import AppUserManager
from maintenance_management.common.models import Company


#  TODO: Validators for fields where needed

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


class AbstractProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    phone_number = models.IntegerField(
        blank=False,
        null=False,
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    profile_picture = models.ImageField(
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True


class DynamicRegisterInvitation(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
    )
    unique_identifier = models.UUIDField(default=uuid.uuid4)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    groups = models.ForeignKey(auth_models.Group, on_delete=models.CASCADE)
