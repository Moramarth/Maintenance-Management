from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

PHONE_VALIDATION = RegexValidator(
    regex=r'^\+\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

MAX_FILE_SIZE_IN_MB = 1


def only_letters_validator(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Name must contain only letters")


def first_char_validation(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_file_size(image_object):
    if image_object.size > MAX_FILE_SIZE_IN_MB * 1024 * 1024:
        raise ValidationError(f"The maximum file size that can be uploaded is {MAX_FILE_SIZE_IN_MB} MB")


def validate_user_is_not_already_registered(value):
    user_model = get_user_model()
    if user_model.objects.filter(email=value):
        raise ValidationError("User with the given e-mail is already registered")
