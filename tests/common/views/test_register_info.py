from django.test import TestCase
from django.urls import reverse


class RegisterInfoTests(TestCase):

    def test_register_info(self):
        response = self.client.get(reverse('register info'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('common/registration_info_page.html')
