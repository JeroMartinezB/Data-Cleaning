# Jeronimo Martinez Barragan
# CSC 362
# Assignment 2
# Cleaning a Dataset

import numpy as np
import pandas as pd

# Load the data
data_frame = pd.read_csv("pd_hoa_dataset.csv")
print(data_frame.shape)

# Explore and check the data
print(data_frame.tail(5))
print(data_frame.head(5))
print("Number of participants: ", data_frame.shape[0]//9)
print(data_frame.iloc[660:670, :])

# Missing data
print(data_frame["duration"].value_counts()["?"]) # 10 missing for column duration
# We replace them
data_frame.replace("?", np.nan, inplace=True)
# See how many null values are in the data frame
print(data_frame.isnull().sum()) # 10 null values in total, the same from column duration
# We drop those values since it's only 10 out of 675
data_frame.dropna(inplace=True)
print("After dropping: \n", data_frame.isnull().sum()) # Check after dropping the values

# Reset index after dropping values
data_frame.reset_index(inplace=True, drop=True)

# Replace the values at column task with human readable values
# Meaning of each number
task_meaning = {"1": "Water plants", "2": "Fill medication dispenser",
                "3": "Wash countertop", "4": "Sweep and dust", 
                "5": "Cook", "6": "Wash hands", "7": "Perform TUG",
                "8": "Perform TUG w/ questions", "dot": "Day out task"}
# Replace
def decode_task(df):
    series = df["task"]
    for key in task_meaning:
        series.replace(key, task_meaning[key], inplace=True)
decode_task(data_frame)
print(data_frame.head(10)) # Confirm

# Clean values in the column "Class"
def clean_class(df):
    series = df["class"].copy() # Create a copy of the values
    for i in range(len(series)):
        curr_class = str(series.iloc[i])
        curr_class = curr_class.lower() # Normalize and make all values lowercase
        #Replace
        if "hoa" in curr_class or "healthy" in curr_class:
            series.iloc[i] = "HOA"
        elif "pd" in curr_class or "parkinson" in curr_class:
            series.iloc[i] = "PD"
        else: 
            print("Unrecognized status")
    df["class"] = series

clean_class(data_frame)
# Confirm
print(data_frame.head(25)) 
print(data_frame["class"].value_counts())

# Check column types
for column in data_frame.columns:
    print(column, data_frame[column].dtype)

print(type(data_frame["duration"].sum())) # Will produce error, because it is stored as str not int
# Solution
data_frame["duration"] = data_frame["duration"].astype(np.int32) # Replace str object with np int 32
print(type(data_frame["duration"].sum())) # Confirm

# Write the clean data
data_frame.to_csv("pd_hoa_dataset_cleaned.csv", index=False)

# Reflection
# The explanation was clear and clean, so I faced little to no challenges at all
# Instead, I learned by hands on experience how important cleaning and normalizing
# data is. Something as little as a missing value or an outlier, can completely change
# the inductive bias, so it is crucial that the data is consistent and clean. 