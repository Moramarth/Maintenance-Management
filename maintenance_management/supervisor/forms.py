from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def choice_population(query_set):
    choices = list()
    for item in query_set:
        choices.append((item.pk, item))
    return choices


class AssignForm(forms.Form):
    clients = UserModel.objects.filter(groups__name="Clients")
    contractors = UserModel.objects.filter(groups__name="Contractors")
    Choices = choice_population(clients) + choice_population(contractors)
    assign_to = forms.ChoiceField(widget=forms.RadioSelect, choices=Choices)
