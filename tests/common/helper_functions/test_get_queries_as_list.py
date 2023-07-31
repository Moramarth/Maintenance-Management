from typing import List

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from maintenance_management.clients.models import Review
from maintenance_management.common.helper_function import get_queries_as_list
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building
from tests.common.create_objects_for_testing import create_objects_for_testing

UserModel = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class GetQueriesAsListTests(TestCase):

    def test_get_queries_as_list__with_valid_queries__expect_lists_created(self):
        number_of_objects = 3
        create_objects_for_testing(number_of_objects)
        all_tenants, all_buildings, all_reviews = get_queries_as_list()
        self.assertEqual(number_of_objects, len(all_tenants))
        self.assertEqual(number_of_objects, len(all_buildings))
        self.assertEqual(number_of_objects, len(all_reviews))
        self.assertTrue(all(isinstance(obj, Company) for obj in all_tenants))
        self.assertTrue(all(isinstance(obj, Building) for obj in all_buildings))
        self.assertTrue(all(isinstance(obj, Review) for obj in all_reviews))
        self.assertTrue(all(
            isinstance(obj, List) for obj in (
                all_tenants,
                all_buildings,
                all_reviews
            )
        )
        )

    def test_get_queries_as_list__with_no_objects_created__expect_empty_lists(self):
        all_tenants, all_buildings, all_reviews = get_queries_as_list()
        self.assertEqual(0, len(all_tenants))
        self.assertEqual(0, len(all_buildings))
        self.assertEqual(0, len(all_reviews))
        self.assertTrue(all(
            isinstance(obj, List) for obj in (
                all_tenants,
                all_buildings,
                all_reviews
            )
        )
        )
