import os

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, RequestFactory, override_settings

from maintenance_management.common.models import Company
from maintenance_management.common.views import CompanyDetails


@override_settings(STORAGES={
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
})
class CompanyTests(TestCase):
    VALID_COMPANY_DATA = {
        "name": "Test Company",
        "business_field": "Test Business Field",
        "additional_information": "Test Additional Information",
        "file": SimpleUploadedFile(
            name="test_picture.jpg",
            content=b"",

        )
    }

    def test_company_create__with_valid_data__expect_to_be_created(self):
        company = Company(**self.VALID_COMPANY_DATA)
        company.full_clean()
        company.save()

        self.assertEqual(1, len(Company.objects.all()))

        company.file.delete()

    def test_company_str_dunder__with_valid_data_expect_no_errors(self):
        company = Company(**self.VALID_COMPANY_DATA)
        company.full_clean()
        company.save()

        self.assertEqual(
            f"{company.name} - Business Field: {company.business_field or 'Not shown'}",
            str(company)
        )

    def test_company_create__with_name_max_length_exceeded__expect_raises(self):
        company = Company(**self.VALID_COMPANY_DATA)
        company.name = "c" * Company.MAX_LENGTH_FOR_NAME + "c"

        with self.assertRaises(ValidationError):
            company.full_clean()

    def test_company_create__with_business_field_max_length_exceeded__expect_raises(self):
        company = Company(**self.VALID_COMPANY_DATA)
        company.business_field = "b" * Company.MAX_LENGTH_FOR_BUSINESS_FIELD + "b"

        with self.assertRaises(ValidationError):
            company.full_clean()

    def test_company_get_absolute_url_method__expect_no_errors(self):
        company = Company.objects.create(**self.VALID_COMPANY_DATA)
        path = company.get_absolute_url()
        request = RequestFactory().get(path)
        response = CompanyDetails.as_view()(request, pk=company.pk)
        self.assertEqual(200, response.status_code)

        company.file.delete()
