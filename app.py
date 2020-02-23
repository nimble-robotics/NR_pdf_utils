from utils import upload_to_aws,bucket_name

local_filename = 'error.html'
s3_filename = 'error.html'
uploaded = upload_to_aws(local_filename, bucket_name, s3_filename, "text/html")

