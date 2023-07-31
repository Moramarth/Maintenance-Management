from decouple import config
from django.test import TestCase
from django.urls import reverse


class RedirectToAdminTests(TestCase):

    def test_redirect_to_admin(self):

        response = self.client.get(reverse('admin page'))
        self.assertEqual(302, response.status_code)
        self.assertEqual(f"{config('DOMAIN_NAME')}admin/", response.url)
