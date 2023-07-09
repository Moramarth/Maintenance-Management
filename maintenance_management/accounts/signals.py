from decouple import config
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from maintenance_management.accounts.models import RegisterInvitation, AppUser, AppUserProfile


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


@receiver(post_save, sender=AppUser)
def create_empty_app_user_profile(instance, created, *args, **kwargs):
    if created:
        company = RegisterInvitation.objects.get(email=instance.email).company
        AppUserProfile.objects.create(user=instance, company=company)


@receiver(post_save, sender=AppUserProfile)
def delete_invitation_info_after_user_and_profile_creation(instance, *args, **kwargs):
    invitation = RegisterInvitation.objects.get(email=instance.user.email)
    invitation.delete()
