from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import Group
from django.test import TestCase, RequestFactory, override_settings
from django.urls import reverse

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.common.models import Company
from maintenance_management.common.views import EditCompanyInfo

UserModel = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class EditCompanyInfoTests(TestCase):
    def setUp(self):
        Group.objects.create(name="Supervisor")
        self.company = Company(
            name="Company Name",
            business_field="Test Business Field",
            additional_information="Test Additional Information",
        )
        self.company.save()

        UserModel.objects.create_user(
            email="validemail@test.com",
            password="Te$tP@ssw0rd",
            groups=Group.objects.first(),
            is_staff=True,
        )

        self.user = UserModel.objects.first()

        AppUserProfile.objects.create(
            user=self.user,
            company=self.company
        )

    def test_get_edit_company_page__expect_no_errors(self):
        response = self.client.get(reverse("company details", args=(self.company.pk,)))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('common/company_details.html')

    def test_post_edit_company_page__expect_no_errors(self):
        self.client.login(
            email="validemail@test.com",
            password="Te$tP@ssw0rd",
        )

        request = RequestFactory().post(
            reverse("company details", args=(self.company.pk,)),
            data={
                "name": "Company Changed Name",
                "additional_information": "",
            },
        )
        request.user = get_user(self.client)

        response = EditCompanyInfo.as_view()(request, pk=self.company.pk)

        self.assertEqual(302, response.status_code)
        self.assertEqual(self.company.get_absolute_url(), response.url)

        self.company.refresh_from_db()
        self.assertEqual("Company Changed Name", self.company.name)
        self.assertEqual("", self.company.additional_information)
