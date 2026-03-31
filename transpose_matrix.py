# Element-wise multiplication

import numpy as np

def multiply(a, b):
    return a * b


# Input
a = np.array(list(map(int, input("Enter array1: ").split())))
b = np.array(list(map(int, input("Enter array2: ").split())))

# Output
print("Result:", multiply(a, b))