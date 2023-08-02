from maintenance_management.common.custom_storage_classes import MediaStorage


def delete_file_when_delete_model_instance(instance):
    """
    Deletes an image(if there is one) when related model instance is deleted
    """

    try:
        instance.file.delete(save=False)
    except:

        pass


def delete_old_file_when_update_model_instance(instance):
    """
    Checks for file changes, if there are such, deletes old file.

    If the same image is attached for upload, skips the upload
    """

    try:
        old_img = instance.__class__.objects.get(pk=instance.pk).file
        try:
            new_img = instance.file
        except:
            new_img = None
        if new_img != old_img:
            MediaStorage().delete(old_img.name)
    except:

        pass
