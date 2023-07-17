from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import BaseUserCreationForm

from maintenance_management.accounts.models import AppUserProfile, RegisterInvitation

UserModel = get_user_model()


# Register your models here.

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    # changed UserAdmin options
    add_form_template = "admin_site_customization/admin_user_add_form.html"
    fieldsets = [
        ("Auth Data", {
            "classes": ["wide"],
            "fields": ["email", "password", "groups"]
        }),
        ("Additional Information", {"fields": ["is_staff", "is_active"]}),

    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ["email", "is_staff", "is_active", "last_login"]
    search_fields = ["email"]
    ordering = ("email",)
    filter_horizontal = []

    # extra options
    search_help_text = "Search for a user by e-mail"
    date_hierarchy = "last_login"
    radio_fields = {"groups": admin.VERTICAL}


@admin.register(AppUserProfile)
class AppUserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "phone_number", "company", "expertise"]
    list_filter = ["expertise", "company"]
    search_fields = ["first_name", "last_name"]
    search_help_text = "Search for a user by name"
    view_on_site = True


@admin.register(RegisterInvitation)
class RegisterInvitationAdmin(admin.ModelAdmin):
    list_display = ["email", "company", "groups", "unique_identifier"]
    radio_fields = {"groups": admin.VERTICAL}

