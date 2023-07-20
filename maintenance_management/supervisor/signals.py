from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from maintenance_management.contractors.models import Meeting, ExpensesEstimate
from maintenance_management.supervisor.models import Assignment


@receiver(post_save, sender=Meeting)
def assigment_requires_a_meeting(instance, created, *args, **kwargs):
    if created:
        assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
        assignment.meeting_required = True
        assignment.save()


@receiver(pre_delete, sender=Meeting)
def assigment_requires_a_meeting(instance, *args, **kwargs):
    assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
    assignment.meeting_required = False
    assignment.save()


@receiver(post_save, sender=ExpensesEstimate)
def assigment_has_an_offer_available(instance, created, *args, **kwargs):
    if created:
        assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
        assignment.meeting_required = False
        assignment.expense_estimate_available = True
        assignment.save()


@receiver(pre_delete, sender=ExpensesEstimate)
def assigment_offer_is_going_to_be_deleted(instance, *args, **kwargs):
    assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
    assignment.expense_estimate_available = False
    assignment.save()
