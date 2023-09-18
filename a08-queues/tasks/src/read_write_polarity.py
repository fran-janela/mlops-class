import boto3
import os
from textblob import TextBlob 
import json

"""
EXAMPLE EVENT:
{
    "username": "john1",
    "message": "best product I ever bought!"
}
"""


def send_sqs_message(message):
    sqs = boto3.client("sqs")
    queue_url = os.environ.get("DESTINATION_SQS_URL")
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    return response


def lambda_handler(event, context):
    # Read batch of messages
    for record in event["Records"]:
        # transform record body from string to dict
        payload = json.loads(record["body"])

        message = payload["message"]

        blob = TextBlob(message)
    
        response = {
            "username": payload["username"],
            "message": payload["message"],
            "polarity": str(blob.polarity),
        }

        # Send each message to destination queue
        send_sqs_message(str(response))

    return event["Records"]