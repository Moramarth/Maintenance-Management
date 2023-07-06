from django.contrib import admin

from maintenance_management.accounts.models import AppUser


# Register your models here.

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
