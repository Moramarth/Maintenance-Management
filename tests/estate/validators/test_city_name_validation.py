from django.core.exceptions import ValidationError
from django.test import TestCase

from maintenance_management.estate.validators import city_name_validation


class CityNameValidationTests(TestCase):
    VALID_CITY_NAME = "City-Test Name"
    INVALID_CITY_NAME_WITH_UNDERSCORE = "City_Test Name with underscore"
    VALID_CITY_NAME_WITH_SYMBOLS = "City-Te$t N@me"

    def test_name_validation__with_valid_data__expect_no_errors(self):
        name = self.VALID_CITY_NAME
        city_name_validation(name)

    def test_name_validation__with_invalid_underscore__expect_raises(self):
        with self.assertRaises(ValidationError):
            name = self.INVALID_CITY_NAME_WITH_UNDERSCORE
            city_name_validation(name)

    def test_name_validation__with_invalid_symbols__expect_raises(self):
        with self.assertRaises(ValidationError):
            name = self.VALID_CITY_NAME_WITH_SYMBOLS
            city_name_validation(name)
