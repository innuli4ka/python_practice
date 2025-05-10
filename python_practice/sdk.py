import boto3
from botocore.exceptions import ClientError

# === CONFIGURATION ===
SOURCE_BUCKET = 'bucket-source-inna'
TARGET_BUCKET = 'bucket-target-inna'
SOURCE_PREFIX = 'customer-details/sr1_'
TARGET_PREFIX = 'sr1/'
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-2:855198068452:file-move-notifier'

# === CLIENTS ===
s3 = boto3.client('s3', region_name='us-west-2')
sns = boto3.client('sns', region_name='us-west-2')

def move_files_with_prefix():
    moved_files = []

    try:
        response = s3.list_objects_v2(Bucket=SOURCE_BUCKET, Prefix=SOURCE_PREFIX)
        contents = response.get('Contents', [])

        if not contents:
            print("No matching files found.")
            return

        for obj in contents:
            source_key = obj['Key']
            filename = source_key.split('/')[-1]
            target_key = TARGET_PREFIX + filename

            # Copy to target
            s3.copy_object(
                Bucket=TARGET_BUCKET,
                CopySource={'Bucket': SOURCE_BUCKET, 'Key': source_key},
                Key=target_key
            )

            # Delete from source
            s3.delete_object(Bucket=SOURCE_BUCKET, Key=source_key)

            print(f"Moved and deleted: {source_key} → {target_key}")
            moved_files.append(filename)

        # Notify if any files moved
        if moved_files:
            message = (
                f"The following files were moved from '{SOURCE_PREFIX}' "
                f"to '{TARGET_PREFIX}' in bucket '{TARGET_BUCKET}':\n" +
                "\n".join(moved_files)
            )
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="S3 File Movement Notification",
                Message=message
            )
            print("✅ SNS notification sent.")

    except ClientError as e:
        print("❌ AWS error occurred:", e)

if __name__ == "__main__":
    move_files_with_prefix()
