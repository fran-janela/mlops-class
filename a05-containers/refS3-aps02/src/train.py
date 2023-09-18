import os
import pandas as pd
import pandas.io.sql as psql
import psycopg2

# Export
import pickle

# Modeling
from sklearn.ensemble import RandomForestRegressor

# S3
import boto3

import os
from dotenv import load_dotenv

# Reading .env and creating environment variables
load_dotenv()

# Reading environment variable
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
port = os.getenv("DB_PORT")

## Import PreProcessed Data
conn = psycopg2.connect(database = database, 
                        user = user, 
                        host= host,
                        password = password,
                        port = port)

print("Database connected successfully")
cur = conn.cursor()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)
print("S3 connected successfully")

# Fetching data from the database
with open(os.path.join(os.path.dirname(__file__), "../data/", "train.sql")) as f:
    df = psql.read_sql(f.read(), conn)
print("Data Fetched")

# Split Features and target
X = df.drop("total_sales", axis=1)
y = df["total_sales"]

## Model Fit
model = RandomForestRegressor(n_estimators=100, random_state=195)
print("Training Model...")
model.fit(X, y)

## Exports
# LOCAL
model_bytes = pickle.dumps(model)

# S3
# Local path, bucket name and key (path on bucket)
s3.put_object(Bucket=os.getenv("AWS_BUCKET_NAME"), Key="franciscopj/model.pkl", Body=model_bytes)
print("Model Exported")

# Close communication with the database
cur.close()
conn.close()