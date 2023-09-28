from services.aws_s3 import AwsBucket
from decouple import config as cf


bucket = AwsBucket()
my_bucket = cf('AWS_BUCKET_NAME')

bucket.upload_file(file_name="./file.csv",bucket=my_bucket)
# bucket.download_file(file_name="./file.csv",bucket=my_bucket)