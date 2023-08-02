from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import Group

from maintenance_management.accounts.models import RegisterInvitation, AppUserProfile
from maintenance_management.common.models import Company

UserModel = get_user_model()


class RegisterInvitationForm(forms.ModelForm):
    class Meta:
        model = RegisterInvitation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        group = Group.objects.all().filter(name=self.request.user.groups.name)
        company = Company.objects.all().filter(pk=self.request.user.appuserprofile.company.pk)
        self.fields["unique_identifier"].widget.attrs["readonly"] = "readonly"
        self.fields["groups"].queryset = group
        self.fields["company"].queryset = company


class UserRegistrationForm(auth_forms.BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', "groups"]
        field_classes = {"email": auth_forms.UsernameField}

        widgets = {
            "groups": forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True
            self.fields["email"].widget.attrs["readonly"] = "readonly"


class EditAppUserProfileForm(forms.ModelForm):
    class Meta:
        model = AppUserProfile
        fields = ["first_name", "last_name", "phone_number", "file"]

        widgets = {
            "first_name": forms.TextInput(attrs={"required": True, "placeholder": "John"}),
            "last_name": forms.TextInput(attrs={"required": True, "placeholder": "Doe"}),
            "phone_number": forms.TextInput(attrs={"required": True, "placeholder": "+359123456789"}),
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone_number": "Phone Number",
            "profile_picture": "Profile Picture",
        }
