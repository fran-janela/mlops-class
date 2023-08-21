import os
import pandas as pd

# Export
import pickle

# Modeling
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

## Import PreProcessed Data
df = pd.read_csv("../data/bank_pro.csv")

## Define category columns
cat_cols = ["job", "marital", "education", "housing"]

# Split Features and target
X = df.drop("deposit", axis=1)
y = df["deposit"]

# Split Train Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1912)

## One Hot Encoder Transform
one_hot_enc = make_column_transformer(
    (OneHotEncoder(handle_unknown="ignore", drop="first"),
    cat_cols),
    remainder="passthrough")

X_train = one_hot_enc.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=one_hot_enc.get_feature_names_out())

## Model Fit
model = LGBMClassifier()
model.fit(X_train, y_train)

## Exports
current_directory = os.path.dirname(__file__)
models_path = "../models/"
# Save the model as a pickle file
model_file_path = os.path.join(current_directory, models_path, "model.pkl")
with open(model_file_path, "wb") as f:
    pickle.dump(model, f)

# Save the OneHotEncoder as a pickle file
ohe_file_path = os.path.join(current_directory, models_path, "ohe.pkl")
with open(ohe_file_path, "wb") as f:
    pickle.dump(one_hot_enc, f)