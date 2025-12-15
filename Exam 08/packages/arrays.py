import numpy as np
# 1D Arreay Create
def create_1d():
    n = int(input("Enter number of elements for 1D array : "))
    data = []
    
    for i in range(n):
        val = int(input(f"Enter value {i+1} : "))
        data.append(val)
        
    arr = np.array(data)
    print("\nYour 1D NumPy Array is:")
    print(arr)
    return arr

# 2D Arreay Create
def create_2d():
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

# 3D Arreay Create
def create_3d():
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

#---------> indexing

def indexing(arr):
    print("\n--- Indexing ---")
    idx = input("Enter index (ex: 0 , 1,2 , 0,1,2): ")

    # multiple indices separated by comma
    try:
        idx = tuple(map(int, idx.split(',')))
        print("Value =", arr[idx])
    except:
        print("Invalid index!")

#---------> slicing

def slicing(arr):
    print("\n--- Slicing ---")
    print("Enter the row and col range(ex: 0:3 , : , 1: , :2  ) : ")

    sl = input("Enter slice: ")

    try:
        s_obj = slice(*[int(x) if x else None for x in (sl.split(':') + ['',''])[:3]])
        print("Result:\n", arr[s_obj])
    except:
        print("Invalid slice!")