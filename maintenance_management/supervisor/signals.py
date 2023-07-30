from django.db.models.signals import post_save, pre_delete
from django.shortcuts import get_object_or_404

from maintenance_management.common.custom_decorators import custom_receiver
from maintenance_management.contractors.models import Meeting, ExpensesEstimate
from maintenance_management.supervisor.models import Assignment


@custom_receiver(post_save, sender=Meeting)
def assigment_requires_a_meeting(sender, instance, created, *args, **kwargs):
    if created:
        assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
        assignment.meeting_required = True
        assignment.save()


@custom_receiver(pre_delete, sender=Meeting)
def assigment_requires_a_meeting(sender, instance, *args, **kwargs):
    assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
    assignment.meeting_required = False
    assignment.save()


@custom_receiver(post_save, sender=ExpensesEstimate)
def assigment_has_an_offer_available(sender, instance, created, *args, **kwargs):
    if created:
        assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
        assignment.meeting_required = False
        assignment.expense_estimate_available = True
        assignment.save()


@custom_receiver(pre_delete, sender=ExpensesEstimate)
def assigment_offer_is_going_to_be_deleted(sender, instance, *args, **kwargs):
    assignment = get_object_or_404(Assignment, pk=instance.assignment.pk)
    assignment.expense_estimate_available = False
    assignment.save()
