from django.contrib import admin

from maintenance_management.accounts.models import AppUser, AppUserProfile, RegisterInvitation


# Register your models here.

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass


@admin.register(AppUserProfile)
class AppUserProfile(admin.ModelAdmin):
    pass


@admin.register(RegisterInvitation)
class RegisterInvitationAdmin(admin.ModelAdmin):
    pass
