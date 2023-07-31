from django.test import TestCase, override_settings
from django.urls import reverse

from maintenance_management.common.views import (
    TENANTS_DISPLAYED_ON_HOME_PAGE,
    BUILDINGS_DISPLAYED_ON_HOME_PAGE,
    REVIEWS_DISPLAYED_ON_HOME_PAGE
)
from tests.common.create_objects_for_testing import create_objects_for_testing


@override_settings(SUSPEND_SIGNALS=True)
class HomePageTests(TestCase):

    def test_home_page__expect_no_errors(self):
        number_of_objects = 3
        create_objects_for_testing(number_of_objects)
        response = self.client.get(reverse('home page'))

        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual(TENANTS_DISPLAYED_ON_HOME_PAGE, len(context["tenants"]))
        self.assertEqual(BUILDINGS_DISPLAYED_ON_HOME_PAGE, len(context["buildings"]))
        if number_of_objects >= REVIEWS_DISPLAYED_ON_HOME_PAGE:
            self.assertEqual(REVIEWS_DISPLAYED_ON_HOME_PAGE, len(context["reviews"]))
        else:
            self.assertEqual(number_of_objects, len(context["reviews"]))
        self.assertTemplateUsed('common/home.html')
