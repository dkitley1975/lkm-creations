from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    A class to define the storage location for the static files in S3.
    """

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    A class to define the storage location for the media files in S3.
    """

    location = settings.MEDIAFILES_LOCATION
