from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from maintenance_management.accounts.models import RegisterInvitation

UserModel = get_user_model()


class RegisterInvitationForm(forms.ModelForm):
    class Meta:
        model = RegisterInvitation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["unique_identifier"].widget.attrs["readonly"] = "readonly"


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
