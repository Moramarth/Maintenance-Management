from django import forms

from maintenance_management.clients.models import Review


class RatingSelectionFilterForm(forms.Form):
    choices = Review.Rating.choices
    choices.insert(0, (0, "No filter"))
    rating_filter = forms.ChoiceField(
        choices=choices,
        required=False,
        label="Filter by rating"
    )
