from decouple import config
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from maintenance_management.accounts.models import RegisterInvitation, AppUserProfile
from maintenance_management.common.custom_decorators import custom_receiver

UserModel = get_user_model()


@custom_receiver(post_save, sender=RegisterInvitation)
def send_email_invitation(sender, instance, *args, **kwargs):
    """ TODO: Error handling SMTPException or other """

    subject = "Register invitation"
    bcc = [instance.secondary_email]
    template = 'accounts/registry_invitation_email.html'
    context = {
        "dynamic_url": f"{config('DOMAIN_NAME')}accounts/register/{instance.unique_identifier}/"
    }

    html_message = render_to_string(template, context)

    message = EmailMessage(subject=subject, body=html_message, to=[instance.email], bcc=bcc)
    message.content_subtype = 'html'
    message.send()


@custom_receiver(post_save, sender=UserModel)
def create_empty_app_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        company = RegisterInvitation.objects.get(email=instance.email).company
        AppUserProfile.objects.create(user=instance, company=company)


@custom_receiver(post_save, sender=AppUserProfile)
def delete_invitation_info_after_user_and_profile_creation(sender, instance, created, *args, **kwargs):
    if created:
        invitation = RegisterInvitation.objects.get(email=instance.user.email)
        invitation.delete()
