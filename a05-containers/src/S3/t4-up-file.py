import boto3
import os, sys
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, "../../data/hello.txt")

# Local path, bucket name and key (path on bucket)
s3.upload_file(file_path, os.getenv("AWS_BUCKET_NAME"), "franciscopj/hello.txt")