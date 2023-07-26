from django.utils import timezone

from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date

WORKING_HOURS_START = 8
WORKING_HOURS_END = 17


def meeting_is_in_the_future_validator(value):
    today = timezone.localdate()
    desired_date = date(value.year, value.month, value.day)
    if desired_date <= today:
        raise ValidationError("Please choose a date that is at least tomorrow.")
    elif not WORKING_HOURS_START < value.hour < WORKING_HOURS_END:
        raise ValidationError(f"Please consider our working hours.\n{WORKING_HOURS_START}:00 : {WORKING_HOURS_END}:00")
