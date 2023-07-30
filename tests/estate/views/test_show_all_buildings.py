from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode

from maintenance_management.estate.models import Building


def reverse_with_parameters(*args, **kwargs):
    get = kwargs.pop("get", {})
    url = reverse(*args, **kwargs)
    if get:
        url += "?" + urlencode(get)
    return url


class ShowAllBuildingsViewTests(TestCase):
    def setUp(self):
        Building.objects.create(
            name="Building 1",
            city="Test City 1",
            address="Address",
        )
        Building.objects.create(
            name="Building 2",
            city="Test City 1",
            address="Address",
        )
        Building.objects.create(
            name="Different Test name",
            city="Test City 2",
            address="Address",
        )

    def test_show_all_buildings__with_no_filters__expect_no_errors(self):
        response = self.client.get(
            reverse('show all buildings'),
        )
        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(context['buildings']))
        self.assertTemplateUsed(response, 'estate/show_all_buildings.html')

    def test_show_all_buildings__with_name_filter__expect_object_list_object_name_icontains(self):
        params = {"name": "buIld"}
        url = reverse_with_parameters('show all buildings', get=params)
        response = self.client.get(url)
        self.assertTrue(all(
            params["name"].casefold()
            in building.name.casefold()
            for building
            in response.context["object_list"]
        )
        )

    def test_show_all_buildings__with_city_filter__expect_object_list_object_city_icontains(self):
        params = {"city": "2"}
        url = reverse_with_parameters('show all buildings', get=params)
        response = self.client.get(url)
        self.assertTrue(all(
            params["city"].casefold()
            in building.city.casefold()
            for building
            in response.context["object_list"]
        )
        )

    def test_show_all_buildings__with_invalid_filter__expect_object_list_of_zero(self):
        params = {"name": "Wrong test name"}
        url = reverse_with_parameters('show all buildings', get=params)
        response = self.client.get(url)
        self.assertEqual(0, len(response.context["object_list"]))

    def test_show_all_buildings__with_paginator__expect_is_paginated(self):
        params = {"paginator": "2"}
        url = reverse_with_parameters('show all buildings', get=params)
        response = self.client.get(url)
        self.assertEqual(2, len(response.context["object_list"]))
        self.assertTrue(response.context["is_paginated"])
