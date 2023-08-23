import os, sys
import pandas as pd

# Export
import pickle

# Modeling
from sklearn.ensemble import RandomForestRegressor

file_name = sys.argv[1]

## Import PreProcessed Data
current_directory = os.path.dirname(__file__)
data_path = "../data/"
path = os.path.join(current_directory, data_path, file_name)
df = pd.read_parquet(path)

# Split Features and target
X = df.drop("total_sales", axis=1)
y = df["total_sales"]

## Model Fit
model = RandomForestRegressor(n_estimators=100, random_state=195)
print("Training Model...")
model.fit(X, y)

## Exports
current_directory = os.path.dirname(__file__)
models_path = "../models/"
# Save the model as a pickle file
model_file_path = os.path.join(current_directory, models_path, "model.pkl")
with open(model_file_path, "wb") as f:
    pickle.dump(model, f)
    print("Model Saved to {}".format(model_file_path))