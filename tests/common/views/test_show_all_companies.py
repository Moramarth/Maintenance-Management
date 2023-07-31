from django.test import TestCase
from django.urls import reverse

from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building, AdditionalAddressInformation
from tests.estate.views.test_show_all_buildings import reverse_with_parameters


class ShowAllCompaniesTests(TestCase):
    def setUp(self):
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        Company.objects.create(name="Different Test name")

        Building.objects.create(
            name="Building 1",
            city="Test City 1",
            address="Address",
        )
        AdditionalAddressInformation.objects.create(
            building=Building.objects.first(),
            company=Company.objects.first(),
            floor=1,
            office_number=103,
        )

    def test_show_all_companies__with_no_filters__expect_no_errors(self):
        response = self.client.get(
            reverse('show all companies'),
        )
        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(context['object_list']))
        self.assertTemplateUsed(response, 'common/show_all_companies.html')

    def test_show_all_companies__with_name_filter__expect_object_list_object_name_icontains(self):
        params = {"name": "comP"}
        url = reverse_with_parameters('show all companies', get=params)
        response = self.client.get(url)
        self.assertTrue(all(
            params["name"].casefold()
            in company.name.casefold()
            for company
            in response.context["object_list"]
        )
        )

    def test_show_all_companies__with_invalid_filter__expect_object_list_of_zero(self):
        params = {"name": "Wrong test name"}
        url = reverse_with_parameters('show all companies', get=params)
        response = self.client.get(url)
        self.assertEqual(0, len(response.context["object_list"]))

    def test_show_all_companies__with_building_filter__expect_object_list_of_one(self):
        params = {"building": Building.objects.first().pk}
        url = reverse_with_parameters('show all companies', get=params)
        response = self.client.get(url)
        self.assertEqual(1, len(response.context["object_list"]))

    def test_show_all_companies__with_paginator__expect_is_paginated(self):
        params = {"paginator": "2"}
        url = reverse_with_parameters('show all companies', get=params)
        response = self.client.get(url)
        self.assertEqual(2, len(response.context["object_list"]))
        self.assertTrue(response.context["is_paginated"])
