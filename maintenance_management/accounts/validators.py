from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

PHONE_VALIDATION = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


def only_letters_validator(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Name must contain only letters")


def first_char_validation(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_file_size(image_object):
    if image_object.size > 5 * 1024 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 5 MB")
