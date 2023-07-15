from django import forms
from django.contrib.auth import get_user_model

from maintenance_management.supervisor.helper_functions import choice_population

UserModel = get_user_model()


class AssignForm(forms.Form):
    engineers = UserModel.objects.filter(groups__name="Engineering")
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(engineers) + choice_population(contractors)
    assign_to = forms.ChoiceField(widget=forms.RadioSelect, choices=Choices)
