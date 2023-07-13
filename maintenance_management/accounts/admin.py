from django.contrib import admin
from django.contrib.auth import get_user_model

from maintenance_management.accounts.models import AppUserProfile, RegisterInvitation

UserModel = get_user_model()


# Register your models here.

@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    pass


@admin.register(AppUserProfile)
class AppUserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(RegisterInvitation)
class RegisterInvitationAdmin(admin.ModelAdmin):
    pass
