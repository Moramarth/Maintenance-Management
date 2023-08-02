from django.db.models.signals import post_delete, pre_save

from maintenance_management.common.custom_decorators import custom_receiver
from maintenance_management.common.delete_items_from_s3 import delete_old_file_when_update_model_instance, \
    delete_file_when_delete_model_instance
from maintenance_management.common.models import Company


@custom_receiver(post_delete, sender=Company)
def clear_company_logo_when_company_deleted(sender, instance, *args, **kwargs):
    delete_file_when_delete_model_instance(instance)


@custom_receiver(pre_save, sender=Company)
def clear_old_company_logo_when_update_company(sender, instance, *args, **kwargs):
    delete_old_file_when_update_model_instance(instance)
