import boto3
from botocore.exceptions import ClientError


BUCKET_NAME = 'student-inna-bucket'
REGION = 'us-west-2'
FILE_NAME = 'donkey.png'

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

# Uploading a file to the bucket:
try:
    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
    print(f" Uploaded '{FILE_NAME}' to '{BUCKET_NAME}' successfully.")
except ClientError as e:
    print(f"Upload failed: {e}")

#listing files in the bucket:
try:
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    print("\nFiles in the bucket:")
    for obj in response.get('Contents', []):
        print("•", obj['Key'])
except ClientError as e:
    print("Could not list bucket contents:", e) 