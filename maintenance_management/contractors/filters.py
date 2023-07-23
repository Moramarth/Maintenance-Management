from django.db.models import Q

from maintenance_management.accounts.enums import GroupEnum


def initial_query_set_meeting_filter(request, queryset):
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        return queryset
    return queryset.filter(
        Q(created_by=request.user)
        | Q(assignment__assigned_by=request.user)
    )


def initial_query_set_expenses_estimate_filter(request, queryset):
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        return queryset
    return queryset.filter(created_by=request.user)


def first_and_last_name_filter_for_expenses_estimate_and_meeting(name, queryset):
    return queryset.filter(
        Q(created_by__appuserprofile__first_name__icontains=name)
        | Q(created_by__appuserprofile__last_name__icontains=name)
    )
