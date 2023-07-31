from django.test import TestCase

from maintenance_management.common.forms import PaginateByForm


class PaginateByFormTest(TestCase):

    def test_paginate_by_form__with_valid_data__expect_no_errors(self):
        form = PaginateByForm(data={"paginator": 7})
        self.assertEqual({}, form.errors)

    def test_paginate_by_form__with_negative_number__expect_error(self):
        form = PaginateByForm(data={"paginator": -7})
        self.assertEqual([f'Ensure this value is greater than or equal to'
                          f' {PaginateByForm.MIN_VALUE_FOR_PAGINATOR}.'],
                         form.errors["paginator"])
