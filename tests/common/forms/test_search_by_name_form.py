from django.test import TestCase

from maintenance_management.common.forms import SearchByNameForm


class SearchByNameFormTests(TestCase):

    def test_search_by_name_form__with_valid_data__expect_no_errors(self):
        form = SearchByNameForm(data={"name": "ValidNameSearch"})
        self.assertEqual({}, form.errors)

    def test_search_by_name__with_max_length_exceeded__expect_error(self):
        form = SearchByNameForm(data={"name": f"{'n' * SearchByNameForm.MAX_LENGTH_FOR_NAME}n"})

        self.assertEqual([f'Ensure this value has at most {SearchByNameForm.MAX_LENGTH_FOR_NAME}'
                          f' characters (it has {SearchByNameForm.MAX_LENGTH_FOR_NAME + 1}).'],
                         form.errors["name"])

    def test_search_by_name__with_invalid_symbols__expect_error(self):
        form = SearchByNameForm(data={"name": f"1asd$"})

        self.assertEqual(['Name must contain only letters'],
                         form.errors["name"])
