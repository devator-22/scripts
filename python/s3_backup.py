# s3_backup.py
# Purpose This script backs up a specified local directory to an AWS S3 bucket.
# Usage:
# python s3_backup.py /path/to/your/directory your-s3-bucket-name --prefix my-app-backups
# REQUIEREMENTS: Configure AWS CLI with your AWS Account

import boto3
import os
from datetime import datetime

def backup_directory_to_s3(directory_path, bucket_name, backup_prefix):
    """
    Backs up a directory to an S3 bucket.

    :param directory_path: Path to the directory to back up.
    :param bucket_name: Name of the S3 bucket.
    :param backup_prefix: Prefix to use for the backup files in S3.
    """
    s3_client = boto3.client('s3')
    timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')

    for root, _, files in os.walk(directory_path):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, directory_path)
            s3_key = f"{backup_prefix}/{timestamp}/{relative_path}"

            print(f"Uploading {local_path} to s3://{bucket_name}/{s3_key}")
            s3_client.upload_file(local_path, bucket_name, s3_key)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Backup a directory to S3.")
    parser.add_argument("directory", help="The directory to back up.")
    parser.add_argument("bucket", help="The S3 bucket to upload to.")
    parser.add_argument("--prefix", default="backups", help="The prefix for the backup in S3.")

    args = parser.parse_args()

    backup_directory_to_s3(args.directory, args.bucket, args.prefix)