import os
import pandas as pd

# Export
import pickle

# Modeling
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

# Import Models
current_directory = os.path.dirname(__file__)

file_path = os.path.join(current_directory, "../models/model.pkl")
with open(file_path, 'rb') as file:
    model = pickle.load(file)

file_path = os.path.join(current_directory, "../models/ohe.pkl")
with open(file_path, 'rb') as file:
    one_hot_enc = pickle.load(file)

# Import predict data
df = pd.read_csv(os.path.join(current_directory, "../data/bank_predict.csv"))

# Drop Unwanted Columns
prep_df = df.drop(labels = ["default", "contact", "day", "month", "pdays", "previous", "loan", "poutcome", "poutcome"], axis=1)

## Define category columns
cat_cols = ["job", "marital", "education", "housing"]

# Encoding
prep_df = pd.DataFrame(one_hot_enc.transform(prep_df), columns=one_hot_enc.get_feature_names_out())

# Predict
y_pred = model.predict(prep_df)
df["y_pred"] = y_pred

# Mapping
dep_mapping = {1: "yes", 0: "no"}
df["y_pred"] = df["y_pred"].astype("category").map(dep_mapping) # Convert the column to category and map the values

# Export
pd.DataFrame.to_csv(df, os.path.join(current_directory, "../data/bank_predict.csv"), index=False)