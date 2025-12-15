import numpy as np
from packages import arrays

def combine_array(arr):
    arr_dim = arr.ndim

    if arr_dim == 1:
        ele = arr.size
        n = ele
        data = []
        for i in range(n):
            val = int(input(f"Enter value {i+1} : "))
            data.append(val)    
        arr_2 = np.array(data)
        com_arr = np.concatenate((arr,arr_2))
        print("Original Array :\n",arr)
        print("\nSecond Array :\n",arr_2)
        print("\nCombined Array :\n",com_arr)
        
    if arr_dim == 2:
        rows,cols = arr.shape

        data = []
        print("\nEnter values row-wise:")
        for r in range(rows):
            row = []
            for c in range(cols):
                val = int(input(f"Enter value [{r},{c}]: "))
                row.append(val)
            data.append(row)

        arr_2 = np.array(data)
        com_arr = np.concatenate((arr,arr_2))
        print("Original Array :\n",arr)
        print("\nSecond Array :\n",arr_2)
        print("\nCombined Array :\n",com_arr)

    if arr_dim == 3:
        depth,rows,cols = arr.shape
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
        arr_2 = np.array(data)
        com_arr = np.concatenate((arr,arr_2))
        print("Original Array :\n",arr)
        print("\nSecond Array :\n",arr_2)
        print("\nCombined Array :\n",com_arr)

def split_array(arr):
    choose = int(input("enter your choice :"))
    if choose == 1:
        try:
            print("Original Array :\n",arr)
            ver_top, ver_bottom = np.vsplit(arr,2)
            print("Vertical Splited Array :\n",ver_top)
            print("---------------")
            print(ver_bottom)
        except Exception as e:
            print("Error : ",e)

    if choose == 2:
        try:
            print("Original Array :\n",arr)
            hor_left, hor_right = np.hsplit(arr,2)
            print("Horizontal Splited Array :\n",hor_left)
            print("---------------")
            print(hor_right)
        except Exception as e:
            print("Error : ",e)