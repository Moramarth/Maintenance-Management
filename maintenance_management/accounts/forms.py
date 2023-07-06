from django import forms
from django.contrib.auth import forms as auth_forms

from maintenance_management.accounts.models import DynamicRegisterInvitation, AppUser


class DynamicRegisterInvitationForm(forms.ModelForm):
    class Meta:
        model = DynamicRegisterInvitation
        fields = "__all__"


class UserRegistrationForm(auth_forms.BaseUserCreationForm):
    class Meta:
        model = AppUser
        fields = ['email', "groups"]
        field_classes = {"email": auth_forms.UsernameField}

        # widgets = {
        #     "groups": forms.HiddenInput()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True
            self.fields["email"].widget.attrs["readonly"] = "readonly"
            self.fields["groups"].widget.attrs["readonly"] = "readonly"
            self.fields["groups"].widget.attrs["disabled"] = "disabled"
