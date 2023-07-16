from django.contrib import admin
from django.contrib.auth import get_user_model

from maintenance_management.accounts.models import AppUserProfile, RegisterInvitation

UserModel = get_user_model()


# Register your models here.

@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_staff", "is_active", "last_login"]
    search_fields = ["email"]
    search_help_text = "Search for a user by e-mail"
    date_hierarchy = "last_login"
    fieldsets = [
        ("Auth Data", {
            "classes": ["wide", "extrapretty"],
            "fields": ["email", "password", "groups"]
        }),
        ("Additional Information", {"fields": ["is_staff", "is_active"]}),

    ]
    radio_fields = {"groups": admin.VERTICAL}


@admin.register(AppUserProfile)
class AppUserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "phone_number", "company", "expertise"]
    list_filter = ["expertise", "company"]
    search_fields = ["first_name", "last_name"]
    search_help_text = "Search for a user by name"


@admin.register(RegisterInvitation)
class RegisterInvitationAdmin(admin.ModelAdmin):
    list_display = ["email", "company", "groups", "unique_identifier"]
    radio_fields = {"groups": admin.VERTICAL}
