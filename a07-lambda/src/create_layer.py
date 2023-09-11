import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Provide a name following the pattern `layer_polarity_<YOUR_INSPER_USERNAME>`
layer_name = "layer_polarity_franciscopj"

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Read the contents of the zip file that you want to deploy
current_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_dir, "../bin/", "polarity_layer_package.zip"), "rb") as f:
    zip_to_deploy = f.read()

lambda_response = lambda_client.publish_layer_version(
    LayerName=layer_name,
    Description="Layer with textblob for polarity",
    Content={"ZipFile": zip_to_deploy},
)

print("Layer ARN:\n", lambda_response["LayerArn"])
print("Layer LayerVersionArn:\n", lambda_response["LayerVersionArn"])
