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


def initial_query_set_assignments(request, queryset):
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        return queryset
    return queryset.filter(
        Q(assigned_by=request.user)
        | Q(user=request.user))
