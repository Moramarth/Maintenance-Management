from django.contrib.auth import views as auth_views, login
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.forms import RegisterInvitationForm, UserRegistrationForm, EditAppUserProfileForm
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.accounts.models import RegisterInvitation, AppUserProfile


def register_user_view(request, unique_identifier):
    invitation = get_object_or_404(RegisterInvitation, unique_identifier=unique_identifier)
    form = UserRegistrationForm(initial={"email": invitation.email})
    if request.method == "POST":
        data = request.POST.copy()
        data["groups"] = Group.objects.get(pk=invitation.groups.pk)
        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile details', pk=user.pk)
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})


class RegistrationInviteView(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.clients, GroupEnum.contractors, GroupEnum.supervisor]
    template_name = 'accounts/dynamic_register_invite.html'
    form_class = RegisterInvitationForm
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


class AppUserProfileDetails(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.clients, GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'accounts/profile_details.html'
    model = AppUserProfile


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return reverse('profile details', args=[self.request.user.pk])


class LogoutUserView(auth_views.LogoutView):
    pass


class EditAppUserProfile(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.clients, GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = "accounts/edit_profile_page.html"
    model = AppUserProfile
    form_class = EditAppUserProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context


class ChangePassword(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/password/change_password.html'
    success_url = reverse_lazy('change password successful')


class ChangePasswordDone(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password/change_password_successful.html'


class PasswordReset(auth_mixins.LoginRequiredMixin, auth_views.PasswordResetView):
    html_email_template_name = 'accounts/password/reset_password_email.html'
    success_url = reverse_lazy('reset password successful')


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = "accounts/password/reset_password_done.html"


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    pass


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    pass
