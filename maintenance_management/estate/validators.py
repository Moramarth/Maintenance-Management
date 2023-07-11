from django.core.validators import ValidationError


def city_name_validation(value):
    for char in value:
        if not char.isalpha() and not char.isspace() and char != "-":
            raise ValidationError("City name can contain only letters, spaces and dashes")
