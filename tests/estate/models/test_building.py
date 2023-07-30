import os

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from maintenance_management.estate.models import Building


class BuildingTests(TestCase):
    VALID_BUILDING_DATA = {
        "name": "Test Building",
        "city": "Test City",
        "address": "Test Address",
        "picture": SimpleUploadedFile(
            name="test_picture.jpg",
            content=b"",

        )
    }

    def test_building_create__with_valid_data__expect_to_be_created(self):
        building = Building(**self.VALID_BUILDING_DATA)
        building.full_clean()
        building.save()

        self.assertEqual(1, len(Building.objects.all()))

        picture_path = os.path.join('media/', building.picture.name)
        os.remove(picture_path)

    def test_building_create__max_length_name_exceeded__expect_raise(self):
        building = Building(**self.VALID_BUILDING_DATA)
        building.name = "n" * Building.MAX_LENGTH_FOR_NAME + "n"

        with self.assertRaises(ValidationError):
            building.full_clean()

    def test_building_create__max_length_city_exceeded__expect_raise(self):
        building = Building(**self.VALID_BUILDING_DATA)
        building.city = "c" * Building.MAX_LENGTH_FOR_CITY + "c"

        with self.assertRaises(ValidationError):
            building.full_clean()

    def test_building_create__max_length_address_exceeded__expect_raise(self):
        building = Building(**self.VALID_BUILDING_DATA)
        building.address = "a" * Building.MAX_LENGTH_FOR_ADDRESS + "a"
        with self.assertRaises(ValidationError):
            building.full_clean()

    def test_building_create__invalid_city__expect_raise(self):
        building = Building(**self.VALID_BUILDING_DATA)
        building.city = "City-Te$t N@me"
        with self.assertRaises(ValidationError):
            building.full_clean()

    def test_building_get_str_dunder__expect_no_errors(self):
        building = Building.objects.create(**self.VALID_BUILDING_DATA)
        self.assertEqual(building.name, str(building))
