from django.test import TestCase

from maintenance_management.common.helper_function import verify_constants
from maintenance_management.common.models import Company


class VerifyConstantsTests(TestCase):

    def setUp(self):
        self.constant_not_to_be_changed = 2
        self.constant_to_be_changed = 7
        for i in range(5):
            Company.objects.create(name=f"Name {i}")

        self.query = Company.objects.all()

    def test_verify_constant__with_enough_objects_in_query__expect_constant_not_change(self):
        new_constant = verify_constants(self.query, self.constant_not_to_be_changed)
        self.assertEqual(self.constant_not_to_be_changed, new_constant)

    def test_verify_constant__with_less_objects_in_query__expect_constant_to_change(self):
        new_constant = verify_constants(self.query, self.constant_to_be_changed)
        self.assertNotEqual(self.constant_to_be_changed, new_constant)
        self.assertEqual(len(self.query), new_constant)
