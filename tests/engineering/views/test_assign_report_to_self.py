from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import Group
from django.http import Http404
from django.test import TestCase, override_settings
from django.urls import reverse

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.clients.models import ServiceReport
from maintenance_management.common.models import Company
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class AssignReportToSelfTests(TestCase):
    def setUp(self):
        self.valid_group = Group.objects.create(name="Engineering")
        self.invalid_group = Group.objects.create(name="NotValid")
        self.company = Company.objects.create(name="test company")

        self.valid_group_user = UserModel.objects.create_user(
            email="validemail@test.com",
            password="Te$tP@ssw0rd",
            groups=self.valid_group,
            is_staff=True,
        )
        self.invalid_group_user = UserModel.objects.create_user(
            email="invalidemail@test.com",
            password="Te$tP@ssw0rd",
            groups=self.invalid_group,
            is_staff=True,
        )
        self.valid_profile = AppUserProfile.objects.create(user=self.valid_group_user, company=self.company)
        self.invalid_profile = AppUserProfile.objects.create(user=self.invalid_group_user, company=self.company)

        self.report_data = {
            "user": self.valid_group_user,
            "company": self.company,
            "title": "Test Title",
            "description": "description for tests",
            "report_type": ServiceReport.ReportType.ELECTRICAL,
        }

    def test_assign_report_to_self__user_not_authenticated__expect_login_redirect(self):
        report = ServiceReport.objects.create(**self.report_data)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        response = self.client.get(reverse('self assign', args=(report.pk,)))
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, f'/accounts/login/?next=/engineering/self-assign/{report.pk}/')

    def test_assign_report_to_self__user_authenticated_but_wrong_group__expect_raises(self):
        report = ServiceReport.objects.create(**self.report_data)

        self.client.login(
            email="invalidemail@test.com",
            password="Te$tP@ssw0rd",
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get(reverse('self assign', args=(report.pk,)))
        self.assertEqual(404, response.status_code)

    def test_assign_report_to_self__user_authenticated_valid_group__expect_report_assigned(self):
        report = ServiceReport.objects.create(**self.report_data)
        self.client.login(
            email="validemail@test.com",
            password="Te$tP@ssw0rd",
        )

        response = self.client.get(reverse('self assign', args=(report.pk,)))

        self.assertEqual(1, len(Assignment.objects.all()))
        assignment = Assignment.objects.get(pk=1)
        self.assertEqual(self.valid_group_user, assignment.user)
        self.assertEqual(self.valid_group_user, assignment.assigned_by)
        self.assertEqual(report, assignment.service_report)

        report.refresh_from_db()
        self.assertEqual(ServiceReport.ReportStatus.ASSIGNED, report.report_status)
        self.assertEqual(self.valid_group_user, report.assigned_to)

        self.assertRedirects(response, f'/clients/service-reports/{report.pk}/')
