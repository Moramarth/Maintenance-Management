from django.test import TestCase
from django.test.client import RequestFactory

from maintenance_management.common.context_processors import context_forms_and_common_queries
from maintenance_management.estate.models import Building


class ContextFormsAndCommonQueriesTests(TestCase):

    def test_context_data__with_created_buildings__expect_existing_context(self):
        for i in range(5):
            Building.objects.create(
                name=f"Building {i}",
                city=f"City {i}",
                address=f"Address {i}",
            )
        context_data = context_forms_and_common_queries(RequestFactory().request())

        self.assertEqual(5, len(context_data["buildings"]))
        self.assertIn("paginator_form", context_data)
        self.assertIn("search_by_name_form", context_data)

    def test_context_data__no_created_buildings__expect_empty_building_query(self):
        context_data = context_forms_and_common_queries(RequestFactory().request())

        self.assertEqual(0, len(context_data["buildings"]))
        self.assertIn("paginator_form", context_data)
        self.assertIn("search_by_name_form", context_data)
