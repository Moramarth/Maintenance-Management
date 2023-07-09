from decouple import config
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from maintenance_management.accounts.forms import RegisterInvitationForm, UserRegistrationForm
from maintenance_management.accounts.models import RegisterInvitation

UserModel = get_user_model()


def registration_invite_view(request):
    form = RegisterInvitationForm()
    if request.method == "POST":
        form = RegisterInvitationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})


def register_user_view(request, unique_identifier):
    invitation = get_object_or_404(RegisterInvitation, unique_identifier=unique_identifier)
    form = UserRegistrationForm(initial={"email": invitation.email})
    if request.method == "POST":
        data = request.POST.copy()
        data["groups"] = [Group.objects.get(pk=invitation.groups_id)]
        form = UserRegistrationForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                f"{config('DOMAIN_NAME')}"
                f"{invitation.groups.name.lower()}"
                f"/profile/{UserModel.objects.get(email=invitation.email).pk}/")
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})
