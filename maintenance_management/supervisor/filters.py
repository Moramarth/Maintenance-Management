import django_filters
from django.db.models import Q

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.supervisor.models import Assignment


class AssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = Assignment
        fields = {
            "assignment_status": ["exact"],
            "meeting_required": ["exact"],
            "expense_estimate_available": ["exact"],
        }

    def __init__(self, *args, **kwargs):
        super(AssignmentFilter, self).__init__(*args, **kwargs)
        self.filters["meeting_required"].label = "Meeting"
        self.filters["expense_estimate_available"].label = "Offer"


def initial_query_set_assignments_filter(request, queryset):
    """ Provides restricted queryset based on business logic authorization"""
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        return queryset
    return queryset.filter(
        Q(assigned_by=request.user)
        | Q(user=request.user))


def first_and_last_name_filter_for_assignment(name, queryset):
    return queryset.filter(
        Q(user__appuserprofile__first_name__icontains=name)
        | Q(user__appuserprofile__last_name__icontains=name)
        | Q(assigned_by__appuserprofile__first_name__icontains=name)
        | Q(assigned_by__appuserprofile__last_name__icontains=name)
    )
