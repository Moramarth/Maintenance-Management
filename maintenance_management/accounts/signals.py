"""
TODO:
 1) create empty profile when user is saved
 2) set event to delete dynamic url info if user and profile are created;
 3) set event to delete user if profile is deleted;

"""
from decouple import config
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from maintenance_management.accounts.models import RegisterInvitation


@receiver(post_save, sender=RegisterInvitation)
def send_email_invitation(instance, *args, **kwargs):
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
