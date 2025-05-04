import os
import shutil
import zipfile
import boto3
from botocore.exceptions import ClientError
from pathlib import Path
from datetime import datetime

BUCKET_NAME = 'daily-sales-reports-bucket-inna'  
REPORTS_DIR = Path("daily_reports")
ZIP_FILE = Path("sales_reports.zip")

def ensure_bucket_exists(bucket_name):
    s3 = boto3.client('s3', region_name='us-west-2')
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code in ['404', 'NoSuchBucket']:
            print(f"Bucket '{bucket_name}' not found. Creating it...")
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
            )
        else:
            raise


def ensure_reports_exist():
    REPORTS_DIR.mkdir(exist_ok=True)
    if not any(REPORTS_DIR.glob("*.txt")):
        print("Creating dummy reports...")
        for i in range(3):
            with open(REPORTS_DIR / f"report_{i+1}.txt", "w") as f:
                f.write(f"Report {i+1} generated on {datetime.now()}\n")

def zip_reports(zip_path, folder_path):
    if zip_path.exists():
        print("Removing existing ZIP...")
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in folder_path.glob("*.txt"):
            zipf.write(file, arcname=file.name)
    print(f"Created ZIP: {zip_path}")

def upload_to_s3(file_path, bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(str(file_path), bucket_name, file_path.name)
        print(f"Uploaded '{file_path.name}' to bucket '{bucket_name}'.")
    except ClientError as e:
        print("Upload failed:", e)

if __name__ == "__main__":
    ensure_bucket_exists(BUCKET_NAME)
    ensure_reports_exist()
    zip_reports(ZIP_FILE, REPORTS_DIR)
    upload_to_s3(ZIP_FILE, BUCKET_NAME)
