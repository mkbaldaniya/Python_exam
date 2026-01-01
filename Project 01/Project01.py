import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from packages import dataset,missing,trend, visualization
print("Welcome to the Stock Market Analysis Tool!")
devider = "=" * 50

while True:
    print("Choose an option:")
    print("1. Load Dataset File")
    print("2. Explore Data")
    print("3. Missing Values Handling")
    print("4. Dublicate Rows Removal")
    print("5. Trend Analysis")
    print("6. Daily Returns Calculation")
    print("7. Moving Average Analysis")
    print("8. Volatility Analysis")
    print("9. Find Any Patterns (Data Visualization)")
    print("10. Export Cleaned Dataset")

    choose = input("Enter your choice : ")
    match choose:
        case "1":
            print("\n========|| Dataset ||========\n")
            data = dataset.load_dataset()
            print(devider)
        case "2":
            print("\n========|| Explore Data ||========\n")
            dataset.explore_data(data)
            print(devider)
            
        case "3":
            print("\n========|| Missing Values Handling ||========\n")
            missing.missing_values_handling(data)
            print(devider)
        case "4":
            print("\n========|| Duplicate Rows Removal ||========\n")
            missing.duplicate_rows_removal(data)
            print(devider)
        case "5":
            print("\n========|| Trend Analysis ||========\n")
            trend.trend_analysis(data)
            print(devider)
            
        case "6":
            print("\n========|| Daily Returns Calculation ||========\n")
            trend.daily_returns_calculation(data)
            print(devider)
            
        case "7":
            print("\n========|| Moving Average Analysis ||========\n") 
            trend.moving_average_analysis(data)
            print(devider)
        
        case "8":
            print("\n========|| Volatility Analysis ||========\n") 
            trend.volatility_analysis(data)
            print(devider)

        case "9":
            print("\n========|| Find Any Patterns (Data Visualization) ||========\n") 
            visualization.find_patterns(data)
            print(devider)
        
        case "10":
            print("\n========|| Export Cleaned Dataset ||========\n")
            dataset.save_dataset(data)
            print(devider)
        case "exit":
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid choice. Please select a valid option.")