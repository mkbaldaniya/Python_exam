import matplotlib.pyplot as plt

def find_patterns(data):
    print("Finding Patterns in Data...")
    try:
        column = input("Enter the column name to analyze for patterns (e.g., 'Close'): ")
        
        plt.figure(figsize=(12,6))
        plt.hist(data[column], bins=30, color="#4682B4", alpha=0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
        
        print("\nPattern Summary:")
        print(f"Column Name       : {column}")
        print(f"Total Values      : {data[column].count()}")
        print(f"Missing Values    : {data[column].isna().sum()}")
        print(f"Mean              : {data[column].mean():.2f}")
        print(f"Median            : {data[column].median():.2f}")
        print(f"Standard Deviation: {data[column].std():.2f}")
        print(f"Min Value         : {data[column].min():.2f}")
        print(f"Max Value         : {data[column].max():.2f}")
    except Exception as e:
        print(f"An error occurred while finding patterns: {e}")