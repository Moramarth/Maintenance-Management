from django.contrib.auth import views as auth_views, login
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.forms import RegisterInvitationForm, UserRegistrationForm, EditAppUserProfileForm
from maintenance_management.accounts.models import RegisterInvitation, AppUserProfile


def register_user_view(request, unique_identifier):
    invitation = get_object_or_404(RegisterInvitation, unique_identifier=unique_identifier)
    form = UserRegistrationForm(initial={"email": invitation.email})
    if request.method == "POST":
        data = request.POST.copy()
        data["groups"] = [Group.objects.get(pk=invitation.groups_id)]
        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile details', pk=user.pk)
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})


class RegistrationInviteView(views.CreateView):
    template_name = 'accounts/dynamic_register_invite.html'
    form_class = RegisterInvitationForm
    success_url = reverse_lazy('home page')


class AppUserProfileDetails(views.DetailView):
    template_name = 'accounts/profile_details.html'
    model = AppUserProfile


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class EditAppUserProfile(views.UpdateView):
    template_name = "accounts/edit_profile_page.html"
    model = AppUserProfile
    form_class = EditAppUserProfileForm


class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'accounts/password/change_password.html'
    success_url = reverse_lazy('change password successful')


class ChangePasswordDone(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password/change_password_successful.html'


class PasswordReset(auth_views.PasswordResetView):
    html_email_template_name = 'accounts/password/reset_password_email.html'
    success_url = reverse_lazy('reset password successful')


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = "accounts/password/reset_password_done.html"


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    pass


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    pass
