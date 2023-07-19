from django.core.exceptions import PermissionDenied


class GroupRequiredMixin:
    """
        group_required - list of Enums, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        names = [str(group.value) for group in self.group_required]
        if request.user.groups.name not in names:
            raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
