from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.supervisor.helper_functions import choice_population
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


class AssignForm(forms.Form):
    engineers = UserModel.objects.filter(groups__name="Engineering")
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(engineers) + choice_population(contractors)
    assign_to = forms.ChoiceField(choices=Choices)


class AssignByEngineerForm(forms.Form):
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(contractors)
    assign_to = forms.ChoiceField(choices=Choices)


class AssignmentEditByEngineerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        limit_choices_to=Q(
            groups__name=str(GroupEnum.contractors.value)
        ),
    )

    class Meta:
        model = Assignment
        fields = ["user"]
