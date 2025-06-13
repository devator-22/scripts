# This script lists all S3 buckets in the AWS account and writes their names and creation dates to a CSV file.
# Requiements: boto3 and aws client configured with appropriate permissions.

import boto3
import csv

def list_s3_buckets():
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        
        with open('s3_buckets.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Bucket Name', 'Creation Date'])
            for bucket in buckets:
                writer.writerow([bucket['Name'], bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S')])
        print("S3 buckets written to s3_buckets.csv")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    list_s3_buckets()