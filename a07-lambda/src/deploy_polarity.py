import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Lambda function name
# Provide a name in the pattern `get_polarity_<YOUR_INSPER_USERNAME>`
function_name = "get_polarity_franciscopj"

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
with open(os.path.join(current_dir, "../bin/", "polarity.zip"), "rb") as f:
    zip_to_deploy = f.read()

lambda_response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.10", # Change the runtime if you want!
    Role=lambda_role_arn,
    Handler="polarity.get_polarity",  # function get_polarity inside polarity.py
    Code={"ZipFile": zip_to_deploy},
)

print("Function ARN:", lambda_response["FunctionArn"])