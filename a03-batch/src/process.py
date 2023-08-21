## IMPORTS
# Data
import pandas as pd
import missingno as msno
import os


current_directory = os.path.dirname(__file__)
## PATH
d_path = os.path.join(current_directory, "../data/bank.csv")
pp_path = os.path.join(current_directory, "../data/bank_pro.csv")

## LOAD DATA
df = pd.read_csv(d_path)

## PROCESS
# Mapping
dep_mapping = {"yes": 1, "no": 0}
df["deposit"] = df["deposit"].astype("category").map(dep_mapping) # Convert the column to category and map the values

# Dropping
df = df.drop(labels = ["default", "contact", "day", "month", "pdays", "previous", "loan", "poutcome", "poutcome"], axis=1) # Drop unwanted columns

## SAVE
# Saving Process Results
pd.DataFrame.to_csv(df, pp_path, index=False)
