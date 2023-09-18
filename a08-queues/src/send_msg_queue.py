import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Replace with your queue URL or name
queue_url = "https://sqs.us-east-2.amazonaws.com/820926566402/message_queue_franciscopj"

# Change the message!
message = "Me, myself and I <3"

# Create a Boto3 client for AWS Lambda
sqs_client = boto3.client(
    "sqs",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)


# Send a message to the SQS queue
response = sqs_client.send_message(
    QueueUrl=queue_url,  # Replace with your queue URL or name
    MessageBody=message,
)

# Get the message ID from the response
message_id = response["MessageId"]

print("Message sent with ID:", message_id)