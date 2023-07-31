from django.core.exceptions import ValidationError
from django.test import TestCase

from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building, AdditionalAddressInformation


class AdditionalAddressInformationTests(TestCase):
    VALID_BUILDING_DATA = {
        "name": "Test Building",
        "city": "Test City",
        "address": "Test Address",
    }

    VALID_COMPANY_DATA = {
        "name": "Test Company",
    }

    VALID_ADDRESS_DATA = {
        "section": "Test section",
        "floor": 1,
        "office_number": 101,
    }

    def test_address_information__with_valid_data__expect_no_errors(self):
        building = Building.objects.create(**self.VALID_BUILDING_DATA)
        company = Company.objects.create(**self.VALID_COMPANY_DATA)

        address = AdditionalAddressInformation(building=building, company=company, **self.VALID_ADDRESS_DATA)
        address.full_clean()
        address.save()

        self.assertIsNotNone(address.pk)

    def test_address_information__with_invalid_section_length__expect_raises(self):
        building = Building.objects.create(**self.VALID_BUILDING_DATA)
        company = Company.objects.create(**self.VALID_COMPANY_DATA)

        address = AdditionalAddressInformation(building=building, company=company, **self.VALID_ADDRESS_DATA)
        address.section = "s" * AdditionalAddressInformation.MAX_LENGTH_FOR_SECTION + "s"

        with self.assertRaises(ValidationError):
            address.full_clean()
