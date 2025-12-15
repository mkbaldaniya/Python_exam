import numpy as np
def search_array(arr):
    target = int(input("\nEnter value to search: "))
    
    result = np.where(arr == target)
    
    if result[0].size > 0:
        print(f"Value {target} found at index positions:")
        for index in zip(*result):
            print(index)
    else:
        print(f"Value {target} not found in the array.")

def sort_array(arr):
    print("\nChoose Sort Type:")
    print("1. Flattened Sort (Poora array ek line mein sort hoga)")
    print("2. Axis-wise Sort (Original shape maintain rahega)")
    
    choice = int(input("Enter choice (1 or 2): "))
    
    if choice == 1:
        sorted_arr = np.sort(arr, axis=None)
        print("\nSorted Array (Flattened):")
        print(sorted_arr)
    else:
        sorted_arr = np.sort(arr) 
        print("\nSorted Array (Original Shape):")
        print(sorted_arr)

def filter_array(arr):
    print("\nFilter options:")
    print("1. Find values Greater than X")
    print("2. Find values Less than X")
    
    choice = int(input("Enter choice (1 or 2): "))
    val = int(input("Enter value X: "))
    
    if choice == 1:
        filtered = arr[arr > val]
        print(f"\nValues greater than {val}:")
        print(filtered)
    elif choice == 2:
        filtered = arr[arr < val]
        print(f"\nValues less than {val}:")
        print(filtered)
    else:
        print("Invalid choice")