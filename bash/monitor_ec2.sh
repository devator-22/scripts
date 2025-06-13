#!/bin/bash
# Requirements: AWS CLI installed and configured with credentials
# Running the script: change permissions with `chmod +x monitor_ec2.sh` and run with `./monitor_ec2.sh`
# Monitor EC2 instance status in a given region
REGION="us-east-1"
OUTPUT_FILE="ec2_status.txt"

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI not installed. Please install it and configure credentials."
    exit 1
fi

# Get EC2 instance statuses
aws ec2 describe-instances --region $REGION --query 'Reservations[].Instances[].[InstanceId,State.Name,InstanceType]' --output text > $OUTPUT_FILE

# Check if any instances are not running
while read -r instance_id state instance_type; do
    if [ "$state" != "running" ]; then
        echo "Alert: Instance $instance_id is in state $state"
    fi
done < $OUTPUT_FILE

echo "EC2 instance statuses written to $OUTPUT_FILE"