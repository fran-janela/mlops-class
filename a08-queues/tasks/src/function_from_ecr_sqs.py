import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Lambda function name: read_write_sqs_<INSPER_USERNAME>
function_name = "textblob_sqs_franciscopj"

# Provide Image URI from before
image_uri = "820926566402.dkr.ecr.us-east-2.amazonaws.com/test2-mlops-franciscopj:latest"

queue_name = "lambda_origin_queue_franciscopj"

environment_variables = {
    "DESTINATION_SQS_URL": "https://sqs.us-east-2.amazonaws.com/820926566402/lambda_destination_queue_franciscopj",
}

# Timeout in seconds. Default is 3.
timeout = 15

# Lambda basic execution role
lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)


lambda_response = lambda_client.create_function(
    FunctionName=function_name,
    Role=lambda_role_arn,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Timeout=timeout,
    Environment={"Variables": environment_variables},
)

function_arn = lambda_response["FunctionArn"]

print(f"Function ARN: {function_arn}")

event_source_arn = (
    f'arn:aws:sqs:{os.getenv("AWS_REGION")}:{os.getenv("AWS_ACCOUNT_ID")}:{queue_name}'
)

# Configure the function's event source mapping with the SQS queue
response = lambda_client.create_event_source_mapping(
    EventSourceArn=event_source_arn,
    FunctionName=function_arn,
    BatchSize=2,  # Number of messages to retrieve per batch (optional)
)

print("Lambda function created and configured with SQS event source mapping.")