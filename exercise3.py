import boto3
from botocore.exceptions import ClientError
import os

# Configuration
BUCKET_NAME = 'student-inna-backup'
REGION = 'us-west-2'
FOLDER_NAME = 'dailyDocuments'

# Create S3 client
s3 = boto3.client('s3', region_name=REGION)

# Step 1: Create the bucket if it doesn't already exist
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

# Step 2: Get list of existing files in the bucket
try:
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    existing_files = set(obj['Key'] for obj in response.get('Contents', []))
except ClientError as e:
    print("Failed to retrieve file list from bucket:", e)
    existing_files = set()

# Step 3: Upload only missing files
print("Starting upload of daily documents…")

for file_name in os.listdir(FOLDER_NAME):
    file_path = os.path.join(FOLDER_NAME, file_name)

    # Make sure it's a file, not a folder
    if os.path.isfile(file_path):
        if file_name in existing_files:
            print(f"File already exists: {file_name}")
        else:
            try:
                s3.upload_file(file_path, BUCKET_NAME, file_name)
                print(f"Uploaded: {file_name}")
            except ClientError as e:
                print(f"Failed to upload {file_name}: {e}")
