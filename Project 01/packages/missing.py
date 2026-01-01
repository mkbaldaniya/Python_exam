import pandas as pd, numpy as np,matplotlib.pyplot as plt, seaborn as sns  

# Mising Values Handling Module

def missing_values_handling(data):
    print("1. Show Missing Values Summary")
    print("2. Fill Missing Values With Mean ")
    print("3. Drop Rows with Missing Values")
    print("4. Replace Missing Values With a Specific Value")
    choice = input("Enter your choice : ")
    match choice:
        case "1":
            print("\n~~~~~~~~~~~~~| Show Missing Values |~~~~~~~~~~~~~\n")
            print(data.isnull().sum())
        case "2":
            print("\n~~~~~~~~~~~~~| Fill Missing Values With Mean |~~~~~~~~~~~~~\n")
            data.fillna(data.mean(numeric_only=True), inplace=True)
            print("Missing values filled successfully using MEAN.")

        case "3":
            print("\n~~~~~~~~~~~~~| Drop Rows With  Missing Values |~~~~~~~~~~~~~\n")
            data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        case "4":
            print("\n~~~~~~~~~~~~~| Replace Mising Values With Specific Value |~~~~~~~~~~~~~\n")
            specific_value = input("Enter the specific value to replace missing data: ")
            data.fillna(specific_value, inplace=True)
            print("Missing values replaced with specific value.")
        case _:
            print("Invalid choice. Please select a valid option.")
            
# Dublicate Rows Removal Module
def duplicate_rows_removal(data):
    try:
        initial_count = len(data)
        data.drop_duplicates(inplace=True)
        final_count = len(data)
        print(f"Removed {initial_count - final_count} duplicate rows.")
    except Exception as e:
        print(f"An error occurred: {e}")
