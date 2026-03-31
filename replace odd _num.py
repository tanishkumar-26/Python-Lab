# Replace odd numbers with -1

import numpy as np

def replace_odd(arr):
    arr[arr % 2 != 0] = -1
    return arr


# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Output
print("Modified array:", replace_odd(arr))