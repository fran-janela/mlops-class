import os, sys
import pandas as pd
import pandas.io.sql as psql
import psycopg2

# Export
import pickle

# S3
import boto3

# Modeling
from sklearn.ensemble import RandomForestRegressor

from dotenv import load_dotenv

## Import Data
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
current_directory = os.path.dirname(__file__)
with open(os.path.join(current_directory, "../data/", "predict.sql")) as f:
    df = psql.read_sql(f.read(), conn)
print("Data Fetched")

# Import Models
obj = s3.get_object(Bucket=os.getenv("AWS_BUCKET_NAME"), Key="franciscopj/model.pkl")
model_bytes = obj["Body"].read()
model = pickle.loads(model_bytes)

# Predict
df.drop("total_sales", axis=1, inplace=True)
y_pred = model.predict(df)
df["total_sales"] = y_pred
print("Prediction Done")

# Save to Database
# for index, row in df.iterrows():
#     store_id = row["store_id"]
#     total_sales = row["total_sales"]

#     cur.execute("UPDATE sales_analytics.scoring_ml_franciscopj SET total_sales = %s WHERE store_id = %s", (total_sales, store_id))
#     conn.commit()
# print("Data Saved")

# Close communication with the database
cur.close()
conn.close()
