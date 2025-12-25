import pandas as pd
import numpy as np

def display_missing_values(data):
    print("\n~~~~~~~~~~~~~| Missing Values Only |~~~~~~~~~~~~~\n")
    miss_values = data[data.isna().any(axis=1)]
    print(miss_values)
    return miss_values

def fill_missing_with_mean(data):
    print("\n~~~~~~~s~~~~~~| Missing Filled By Mean |~~~~~~~~~~~~~\n")
    data["Salary"] = data["Salary"].fillna(data["Salary"].mean())
    data["Bonus"] = data["Bonus"].fillna(data["Bonus"].mean())
    print("Missing values filled with mean successfully!")

def drop_rows_with_missing_values(data):
    print("\n~~~~~~~~~~~~~| Drop Rows By Mising Values |~~~~~~~~~~~~~\n")
    data = data.dropna()
    print("Rows with missing values dropped successfully!")
    return data

def replace_missing_with_value(data, value):
    print("\n~~~~~~~~~~~~~| Replace Missing Values With a Specific Value |~~~~~~~~~~~~~\n")
    data = data.fillna(value)
    print(f"Missing values replaced with {value} successfully!")
    return data