import boto3
import os
import logging

from decouple import config as cf
from botocore.client import Config
from botocore.exceptions import ClientError

s3 = boto3.client(
    service_name='s3',
    aws_access_key_id=cf('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=cf('AWS_SECRET_ACCESS_KEY'),
    config=Config(region_name=cf('AWS_REGION'), signature_version='v4')
)

class IBucket:
    def upload_file(self, file_name: str, bucket: str, object_name: str=None):
        """
        Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        pass

    def download_file(self, file_name: str, bucket: str, object_name: str=None):
        """
        Download a file from an S3 bucket

        :param file_name: The path to the file to download to.
        :param bucket: The name of the bucket to download from.
        :param object_name: The name of the key to download from.
        :return: True if file was downloaded, else False
        """
        pass

class AwsBucket(IBucket):
    def upload_file(self, file_name: str, bucket: str, object_name: str = None):
        """
        Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            s3.upload_file(Filename=file_name, Bucket=bucket, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    
    def download_file(self, file_name: str, bucket: str, object_name: str = None):
        """
        Download a file from an S3 bucket

        :param file_name: The path to the file to download to.
        :param bucket: The name of the bucket to download from.
        :param object_name: The name of the key to download from.
        :return: True if file was downloaded, else False
        """
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            s3.download_file(Filename=file_name, Bucket=bucket, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True