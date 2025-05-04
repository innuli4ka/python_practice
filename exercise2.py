import boto3
from botocore.exceptions import ClientError
import os



BUCKET_NAME = 'student-inna-backup'
REGION = 'us-west-2'
FOLDER_NAME = 'dailyDocuments'

s3 = boto3.client('s3', region_name=REGION)
#creating the bucket:try:
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={'LocationConstraint': REGION}
    )
    print(f"Bucket '{BUCKET_NAME}' created successfully.")
except ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        print(f"Bucket '{BUCKET_NAME}' already exists.")
    else:
        raise

# Uploading a files from the dir to the bucket:
print("Starting upload of daily documents…")

for file_name in os.listdir(FOLDER_NAME):
    file_path = os.path.join(FOLDER_NAME, file_name)

    # Make sure it's a file, not a folder
    if os.path.isfile(file_path):
        try:
            s3.upload_file(file_path, BUCKET_NAME, file_name)
            print(f"Uploaded: {file_name}")
        except ClientError as e:
            print(f"Failed to upload {file_name}: {e}")