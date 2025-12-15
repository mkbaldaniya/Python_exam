import numpy as np

# ----------- 1D ARRAY FUNCTION -----------
def create_1d_array():
    n = int(input("Enter number of elements for 1D array: "))
    data = []

    for i in range(n):
        val = int(input(f"Enter value {i+1}: "))
        data.append(val)

    arr = np.array(data)
    print("\nYour 1D Array:")
    print(arr)
    return arr


# ----------- 2D ARRAY FUNCTION -----------
def create_2d_array():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    data = []
    print("\nEnter values row-wise:")
    for r in range(rows):
        row = []
        for c in range(cols):
            val = int(input(f"Enter value [{r},{c}]: "))
            row.append(val)
        data.append(row)

    arr = np.array(data)
    print("\nYour 2D Array:")
    print(arr)
    return arr


# ----------- 3D ARRAY FUNCTION -----------
def create_3d_array():
    depth = int(input("Enter depth (number of 2D layers): "))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    data = []
    print("\nEnter values layer-wise:")
    for d in range(depth):
        print(f"\n--- Layer {d+1} ---")
        layer = []
        for r in range(rows):
            row = []
            for c in range(cols):
                val = int(input(f"Enter value [{d},{r},{c}]: "))
                row.append(val)
            layer.append(row)
        data.append(layer)

    arr = np.array(data)
    print("\nYour 3D Array:")
    print(arr)
    return arr


# ----------- INDEXING FUNCTION -----------
def indexing(arr):
    print("\n--- Indexing ---")
    idx = input("Enter index (ex: 0 , 1,2 , 0,1,2): ")

    # multiple indices separated by comma
    try:
        idx = tuple(map(int, idx.split(',')))
        print("Value =", arr[idx])
    except:
        print("Invalid index!")


# ----------- SLICING FUNCTION -----------
def slicing(arr):
    print("\n--- Slicing ---")
    print("Use format: start:end  (ex: 0:3 , : , 1: , :2  )")

    sl = input("Enter slice: ")

    try:
        s_obj = slice(*[int(x) if x else None for x in (sl.split(':') + ['',''])[:3]])
        print("Result:\n", arr[s_obj])
    except:
        print("Invalid slice!")


# ----------- USER CHOICE SECTION -----------

print("---- NumPy Array Creator ----")
print("1. Create 1D Array")
print("2. Create 2D Array")
print("3. Create 3D Array")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    arr = create_1d_array()

elif choice == 2:
    arr = create_2d_array()

elif choice == 3:
    arr = create_3d_array()

else:
    print("Invalid choice!")
    exit()


# ----------- INDEXING OR SLICING OPTIONS -----------

print("\n--- Choose Operation ---")
print("1. Indexing")
print("2. Slicing")

op = int(input("Enter your choice (1/2): "))

if op == 1:
    indexing(arr)

elif op == 2:
    slicing(arr)

else:
    print("Invalid operation selected!")
    
