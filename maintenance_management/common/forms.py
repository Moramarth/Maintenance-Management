from django import forms

from maintenance_management.accounts.validators import only_letters_validator


class SearchByNameForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        validators=[only_letters_validator],
        label="Search by name",
        required=False,
    )


class PaginateByForm(forms.Form):
    paginator = forms.IntegerField(
        min_value=1,
        required=False,
        label="Items on page"
    )
