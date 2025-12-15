import numpy as np
import pandas as pd
from packages import maths, arrays, combine, filter
devider = "_" * 40
while True:
    print("\nWelcome to the NumPy Analyzer!\n=========================================")
    print("===> Choose an option <===")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or splite Arrays")
    print("4. Search, sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    Choice = int(input("Enter Your Choice : "))
    match Choice:
        case 1:
            print("---> Select the type of Array to create <---\n")
            print("1.--> 1D Array")
            print("2.--> 2D Array")
            print("3.--> 3D Array")
            
            choose = int(input("Enter your Array Choice : "))
            match choose:
                case 1:
                    arr = arrays.create_1d()
                    print(devider)
                    print("\n--- Choose Operation ---")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")
                    

                    op = int(input("Enter your choice (1/2/3): "))

                    if op == 1:
                        arrays.indexing(arr)
                        print(devider)

                    elif op == 2:
                        arrays.slicing(arr)
                        print(devider)
                        
                    elif op == 3:
                        pass

                    else:
                        print("Invalid operation selected!")
                case 2:
                    arr = arrays.create_2d()
                    print(devider)
                    print("\n--- Choose Operation ---")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")

                    op = int(input("Enter your choice (1/2/3): "))

                    if op == 1:
                        arrays.indexing(arr)
                        print(devider)

                    elif op == 2:
                        arrays.slicing(arr)
                        print(devider)
                    
                    elif op == 3:
                        pass

                    else:
                        print("Invalid operation selected!")
                case 3:
                    arr = arrays.create_3d()
                    print(devider)
                    print("\n--- Choose Operation ---")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")

                    op = int(input("Enter your choice (1/2/3): "))

                    if op == 1:
                        arrays.indexing(arr)
                        print(devider)

                    elif op == 2:
                        arrays.slicing(arr)
                        print(devider)
                    
                    elif op == 3:
                        pass

                    else:
                        print("Invalid operation selected!")
                case _:
                    print("Invalid operation selected!")
        case 2:
            maths.math_operations(arr)
            print(devider)
        case 3:
            print("1. Combine Array ")
            print("2. Split Array ")
            choose = int(input("enter your choice :"))
            match choose:
                case 1:
                    combine.combine_array(arr)
                    print(devider)
                case 2:
                    print("1. Vertical Split")
                    print("2. Horizontal Split")
                    combine.split_array(arr)
                    print(devider)

                case _:
                    print("invalid")
        case 4:
            print("1. Search in Array")
            print("2. Sort Array")
            print("3. Filter Array")
            print("4. Go Back")
            
            opt = int(input("Select Option: "))
            
            if opt == 1:
                filter.search_array(arr)
                print(devider)
            elif opt == 2:
                filter.sort_array(arr)
                print(devider)
            elif opt == 3:
                filter.filter_array(arr)   
                print(devider)
            else:
                print("Invalid option!")
        case 5:
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            choice = int(input("Enter choice: "))

            if choice == 1:
                result = f"Sum of Array : {np.sum(arr)}"
            elif choice == 2:
                result = f"Mean of Array : {np.mean(arr)}"
            elif choice == 3:
                result = f"Median of Array : {np.median(arr)}"
            elif choice == 4:
                result = f"Standard Deviation of Array : {np.std(arr)}"
            elif choice == 5:
                result = f"Variance of Array : {np.var(arr)}"
            else:
                print("Invalid choice.")

            print("\nOriginal Array:")
            print(arr)
            print(result)
            print(devider)
        case 6:
            print("\nThank You for using the NumPy Analyzer! Goodbye!")
            break
        case _:
            print("Invalid option. Please select a valid option from the menu.")
