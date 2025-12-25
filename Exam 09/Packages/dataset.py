import numpy as np, pandas as pd

def load_dataset():
    try:
        file_path = input("Enter the path of the dataset (CSV file) : ")
        # file_path = "C:\Maulik Project\Python\Exams\Exam 09\Packages\data\employees.csv"
        data = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!")
        return data
    except Exception as e:
        print("Error : ",e)