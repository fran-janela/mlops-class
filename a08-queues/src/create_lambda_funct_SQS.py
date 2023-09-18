import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Lambda function name: send_sqs_<INSPER_USERNAME>
function_name = "send_sqs_franciscopj"

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

# Read the contents of the zip file that you want to deploy
current_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_dir, "../functions/", "lambda_send_sqs.zip"), "rb") as f:
    zip_to_deploy = f.read()

lambda_response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.10",
    Role=lambda_role_arn,
    Handler="lambda_send_sqs.lambda_handler",
    Code={"ZipFile": zip_to_deploy},
    Timeout=timeout,
    Environment={"Variables": environment_variables}, # This is New!
)

print("Function ARN:", lambda_response["FunctionArn"])