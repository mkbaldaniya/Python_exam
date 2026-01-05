import numpy as np, pandas as pd, os
def load_dataset():
    print("1. load CSV file")
    print("2. load Excel file")
    print("3. load JSON file")
    file_type = input("Enter your choice : ")
    file_path = input("Enter the path to your dataset file: ")
    try:
        match file_type:
            case "1":
                data = pd.read_csv(file_path)
            case "2":
                data = pd.read_excel(file_path)
            case "3":
                data = pd.read_json(file_path)
            case _:
                print("Invalid choice. Please select a valid option.")
                return None
        print("Dataset loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
    

# Explore Data and Show Summary

def explore_data(data):
    if data is None:
        print("No data to explore. Please load a dataset first.")
        return
    print("1. Top Rows Show")
    print("2. Bottom Rows Show")
    print("3. Column Names")
    print("4. info of data")
    choice = input("Enter your choice : ")
    match choice:
        case "1":
            print("\n~~~~~~~~~~~~~| Display First Rows |~~~~~~~~~~~~~\n")
            num = int(input("Enter number of top rows to display: "))
            print(data.head(num))
        case "2":
            print("\n~~~~~~~~~~~~~| Display Last Rows |~~~~~~~~~~~~~\n")
            num = int(input("Enter number of bottom rows to display: "))
            print(data.tail(num))
        case "3":
            print("\n~~~~~~~~~~~~~| Colomns Names |~~~~~~~~~~~~~\n")
            print(data.columns)
        case "4":
            print("\n~~~~~~~~~~~~~| Info of Data |~~~~~~~~~~~~~\n")
            print(data.info())
        case _:
            print("Invalid choice. Please select a valid option.")
            
# Save Cleaned Dataset
def save_dataset(data):
    if data is None:
        print("No data available to save.")
        return

    print("Choose file format:")
    print("1. Save To CSV")
    print("2. Save To Excel")
    print("3. Save To JSON")

    choice = input("Enter your choice: ")
    filename = input("Enter file name (without extension): ")
    try:
        match choice:
            case "1":
                file = filename + ".csv"
                data.to_csv(file, index=False)

            case "2":
                file = filename + ".xlsx"
                data.to_excel(file, index=False)

            case "3":
                file = filename + ".json"
                data.to_json(file, orient="records", lines=True)

            case _:
                print("Invalid choice!")
                return

        print(f"Dataset saved successfully as '{file}'")

    except Exception as e:
        print(f" Error saving dataset: {e}")
        

# Calculate Borrowing Stats Using NumPy
def calculate_borrowing_stats(data):
    if data is None:
        print("No data available for calculation.")
        return

    numeric_data = data.select_dtypes(include=[np.number])

    if numeric_data.empty:
        print("No numeric columns available for calculation.")
        return

    print("Calculating statistics using NumPy...")
    for column in numeric_data.columns:
        col_data = numeric_data[column].dropna()
        mean = np.mean(col_data)
        median = np.median(col_data)
        std_dev = np.std(col_data)

        print(f"\nStatistics for column '{column}':")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Standard Deviation: {std_dev}")