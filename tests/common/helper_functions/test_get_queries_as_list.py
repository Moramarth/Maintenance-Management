from typing import List

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, override_settings
from maintenance_management.clients.models import Review, ServiceReport
from maintenance_management.common.helper_function import get_queries_as_list
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building

UserModel = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class GetQueriesAsListTests(TestCase):
    def setUp(self):
        Group.objects.create(name="placeholder")
        self.group_object = Group.objects.first()

    def test_get_queries_as_list__with_valid_queries__expect_lists_created(self):
        for i in range(1, 4):
            Building.objects.create(
                name=f"Building {i}",
                city=f"City {i}",
                address=f"Address {i}",
            )
            Company.objects.create(
                name=f"Company {i}"
            )
            UserModel.objects.create(
                email=f"email{i}@test.com",
                password="Te$tP@ssw0rd",
                groups=self.group_object,
            )
            ServiceReport.objects.create(
                title=f"Title {i}",
                user=UserModel.objects.get(pk=i),
                company=Company.objects.get(pk=i),
                report_type=ServiceReport.ReportType.OTHER,
            )
            Review.objects.create(
                user=UserModel.objects.get(pk=i),
                service_report=ServiceReport.objects.get(pk=i),
                rating=Review.Rating.TWO
            )

        all_tenants, all_buildings, all_reviews = get_queries_as_list()
        self.assertEqual(3, len(all_tenants))
        self.assertEqual(3, len(all_buildings))
        self.assertEqual(3, len(all_reviews))
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
