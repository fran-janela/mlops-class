## IMPORTS
# Data
import pandas as pd
import os


current_directory = os.path.dirname(__file__)
## PATH
d_path = os.path.join(current_directory, "../data/train-2023-08-01.csv")
pp_path = os.path.join(current_directory, "../data/train-2023-08-01-pro.pqt")

## LOAD DATA
df = pd.read_csv(d_path)

## PROCESS
# Separe Date feature
df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.weekday

# Sum of all sales per store_id in a day
df["total_sales"] = df.groupby(["store_id", "date"])["price"].transform("sum")

# Drop date, client_id, product_id and price feature
df.drop(["date", "client_id", "product_id", "price"], axis=1, inplace=True)

## SAVE
# Saving Process Results to parquet
df.to_parquet(pp_path, index=False)
