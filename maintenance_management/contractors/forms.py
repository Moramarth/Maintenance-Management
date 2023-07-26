from django import forms
from maintenance_management.contractors.models import Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["meeting_date", "description"]

        widgets = {
            "meeting_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            )
        }
