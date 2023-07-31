from django.test import TestCase

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.clients.models import ServiceReport
from maintenance_management.common.models import Company
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


class AcceptAndRejectSetUpMixin(TestCase):

    def setUp(self):
        self.engineers_group = Group.objects.create(name="Engineering")
        self.contractors_group = Group.objects.create(name="Contractors")
        self.invalid_group = Group.objects.create(name="NotValid")
        self.company = Company.objects.create(name="test company")

        self.engineer = UserModel.objects.create_user(
            email="engineer@test.com",
            password="Te$tP@ssw0rd",
            groups=self.engineers_group,
            is_staff=True,
        )
        self.contractor = UserModel.objects.create_user(
            email="contractor@test.com",
            password="Te$tP@ssw0rd",
            groups=self.contractors_group,
            is_staff=False,
        )
        self.client_user = UserModel.objects.create_user(
            email="client@test.com",
            password="Te$tP@ssw0rd",
            groups=self.contractors_group,
            is_staff=False,
        )

        self.not_authorized_user = UserModel.objects.create_user(
            email="not_authorized@test.com",
            password="Te$tP@ssw0rd",
            groups=self.invalid_group,
            is_staff=False,
        )
        self.engineers_profile = AppUserProfile.objects.create(
            user=self.engineer,
            company=self.company
        )
        self.contractor_profile = AppUserProfile.objects.create(
            user=self.contractor,
            company=self.company
        )
        self.client_user_profile = AppUserProfile.objects.create(
            user=self.client_user,
            company=self.company
        )
        self.not_authorized_user_profile = AppUserProfile.objects.create(
            user=self.not_authorized_user,
            company=self.company
        )

        self.service_report = ServiceReport.objects.create(
            user=self.client_user,
            company=self.company,
            title="Test Title",
            description="description for tests",
            report_type=ServiceReport.ReportType.ELECTRICAL,
        )

        self.assignment = Assignment.objects.create(
            service_report=self.service_report,
            user=self.contractor,
            assigned_by=self.engineer,
            meeting_required=False,
            expense_estimate_available=False,
        )
