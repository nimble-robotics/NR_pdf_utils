import boto3
import configparser
from botocore.exceptions import NoCredentialsError

config = configparser.ConfigParser()
config.read('config.ini')


bucket_name = config['aws_s3']['bucket_name']
ACCESS_KEY = config['aws_s3']['access_key']
SECRET_KEY = config['aws_s3']['secret_key']


def upload_to_aws(local_file, bucket, s3_file,cont_type):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file, ExtraArgs={'ContentType': cont_type})
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

