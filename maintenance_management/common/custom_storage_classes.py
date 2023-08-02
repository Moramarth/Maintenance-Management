from decouple import config
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = config('AWS_STORAGE_BUCKET_NAME')
    location = 'maintenance_management_media_files'

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def path(self, name):
        pass


class StaticStorage(S3Boto3Storage):
    bucket_name = config('AWS_STORAGE_BUCKET_NAME')
    location = 'maintenance_management_static_files'

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def path(self, name):
        pass
