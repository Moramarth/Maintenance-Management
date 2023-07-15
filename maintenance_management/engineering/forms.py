from django.contrib.auth import get_user_model
from django import forms

from maintenance_management.supervisor.helper_functions import choice_population

UserModel = get_user_model()


class AssignToContractorForm(forms.Form):
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(contractors)
    assign_to = forms.ChoiceField(widget=forms.RadioSelect, choices=Choices)
