from django.http import Http404


def group_required(*groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            names = [str(group.value) for group in groups]
            if request.user.groups.name in names:
                return function(request, *args, **kwargs)
            raise Http404("Group not suitable")

        return wrapper

    return decorator
