import base64

from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework.response import Response


class UpdateWithImageFieldMixin:

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if self.request.user != instance.user:
            return HttpResponse(status=403)
        if request.data['file'] is not None:
            image_as_string = request.data.pop("file")
            file_name = request.data.pop("filename")
            extension = request.data.pop("extension")
            try:
                image_data = base64.b64decode(image_as_string)
                instance.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
            except Exception:
                return HttpResponse(status=400)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
