from django import forms

from maintenance_management.accounts.validators import only_letters_validator


class SearchByNameForm(forms.Form):
    MAX_LENGTH_FOR_NAME = 20

    name = forms.CharField(
        max_length=MAX_LENGTH_FOR_NAME,
        validators=[only_letters_validator],
        label="Search by name",
        required=False,
    )


class PaginateByForm(forms.Form):
    MIN_VALUE_FOR_PAGINATOR = 3

    paginator = forms.IntegerField(
        min_value=MIN_VALUE_FOR_PAGINATOR,
        required=False,
        label="Items on page",
    )
