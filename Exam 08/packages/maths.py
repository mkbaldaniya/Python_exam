import numpy as np
def math_operations(arr):
    print("\n--- Mathematical Operations ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice: "))

    needed = arr.size
    print(f"\nEnter {needed} values (space separated): ")
    new_values = list(map(float, input().split()))

    if len(new_values) != needed:
        print(f"Error: You must enter exactly {needed} values.")
        return

    new_arr = np.array(new_values).reshape(arr.shape)

    if choice == 1:
        result = arr + new_arr
    elif choice == 2:
        result = arr - new_arr
    elif choice == 3:
        result = arr * new_arr
    elif choice == 4:
        result = arr / new_arr
    else:
        print("Invalid choice.")
        return

    print("\nOriginal Array:")
    print(arr)
    print("\nNew Array:")
    print(new_arr)
    print("\nResult Array:")
    print(result)
