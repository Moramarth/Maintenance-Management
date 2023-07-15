from django import forms
from django.contrib.auth import get_user_model

from maintenance_management.supervisor.helper_functions import choice_population

UserModel = get_user_model()


class AssignForm(forms.Form):
    clients = UserModel.objects.filter(groups__name="Clients")
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(clients) + choice_population(contractors)
    assign_to = forms.ChoiceField(widget=forms.RadioSelect, choices=Choices)
