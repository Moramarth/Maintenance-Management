from django.contrib.auth import get_user_model, get_user

from django.test import override_settings
from django.urls import reverse

from maintenance_management.supervisor.models import Assignment
from tests.engineering.views.helper_mixin_class import AcceptAndRejectSetUpMixin

UserModel = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class AcceptAssignmentTests(AcceptAndRejectSetUpMixin):

    def test_accept_assignment__valid_credentials__expect_assignment_accept(self):
        self.client.login(
            email="contractor@test.com",
            password="Te$tP@ssw0rd",
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get(reverse('accept assignment', args=[self.assignment.pk]))

        self.assertEqual(200, response.status_code)
        self.assignment.refresh_from_db()
        self.assertEqual(Assignment.AssignmentStatus.ACCEPTED, self.assignment.assignment_status)
        self.assertTemplateUsed(response, "engineering/accept_confirmation.html")

    def test_accept_assignment__user_with_wrong_group__expect_404(self):
        self.client.login(
            email="not_authorized@test.com",
            password="Te$tP@ssw0rd",
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get(reverse('accept assignment', args=[self.assignment.pk]))
        self.assertEqual(404, response.status_code)

    def test_accept_assignment__user_not_same_as_assignment_user__expect_403(self):
        self.client.login(
            email="engineer@test.com",
            password="Te$tP@ssw0rd",
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get(reverse('accept assignment', args=[self.assignment.pk]))
        self.assertEqual(403, response.status_code)
