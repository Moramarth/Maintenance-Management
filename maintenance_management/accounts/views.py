from decouple import config
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from maintenance_management.accounts.forms import DynamicRegisterInvitationForm, UserRegistrationForm
from maintenance_management.accounts.models import DynamicRegisterInvitation

UserModel = get_user_model()


def test_email(request):
    form = DynamicRegisterInvitationForm()
    if request.method == "POST":
        form = DynamicRegisterInvitationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "This is a test email"
            from_email = "george.y.lazarov@gmail.com"
            template = 'accounts/registry_invitation_email.html'
            domain = config("DOMAIN_NAME")
            context = {
                "dynamic_url": f"{domain}accounts/register/{form.cleaned_data['unique_identifier']}/"
            }

            html_message = render_to_string(template, context)

            message = EmailMessage(subject, html_message, from_email, [form.cleaned_data['email']])
            message.content_subtype = 'html'
            message.send()

            return HttpResponse("mail should be sent")
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})


# TODO: proper display of groups in the database
def registration_view(request, unique_identifier):
    invitation = get_object_or_404(DynamicRegisterInvitation, unique_identifier=unique_identifier)
    form = UserRegistrationForm(initial={"email": invitation.email, "groups": invitation.groups_id})
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                f"{config('DOMAIN_NAME')}"
                f"{invitation.groups.name.lower()}"
                f"/profile/{UserModel.objects.get(email=invitation.email).pk}/")
    return render(request, 'accounts/dynamic_register_invite.html', {"form": form})
