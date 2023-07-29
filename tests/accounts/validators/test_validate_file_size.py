from django.core.exceptions import ValidationError
from django.test import TestCase

from maintenance_management.accounts.validators import MAX_FILE_SIZE_IN_MB, validate_file_size


class ValidateFileSizeTests(TestCase):
    class MockObject:
        def __init__(self, desired_mbs):
            self.desired_mbs = desired_mbs

        @property
        def size(self):
            return self.desired_mbs * 1024 * 1024

    def test_validation_file_size__with_valid_file_size__expect_no_errors(self):
        mock_object = self.MockObject(MAX_FILE_SIZE_IN_MB)
        validate_file_size(mock_object)

    def test_validation_file_size__with_invalid_file_size__expect_raise(self):
        mock_object = self.MockObject(MAX_FILE_SIZE_IN_MB + 1)
        with self.assertRaises(ValidationError):
            validate_file_size(mock_object)
