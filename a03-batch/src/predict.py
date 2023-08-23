import os, sys
import pandas as pd

# Export
import pickle

# Modeling
from sklearn.ensemble import RandomForestRegressor

# Import Models
current_directory = os.path.dirname(__file__)
model_name = sys.argv[1]

file_path = os.path.join(current_directory, "../models/", model_name)
with open(file_path, 'rb') as file:
    model = pickle.load(file)


## Import PreProcessed Data
file_name = sys.argv[2]
data_path = "../data/"
path = os.path.join(current_directory, data_path, file_name)
df = pd.read_parquet(path)

# Predict
y_pred = model.predict(df)
df["total_sales_predict"] = y_pred

# Export
df.to_parquet(os.path.join(current_directory, "../data/predict-done-2023-08-03.parquet"), index=False)