# Matrix multiplication

import numpy as np

def matrix_multiply(a, b):
    return np.dot(a, b)


# Input
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# Output
print("Result:\n", matrix_multiply(a, b))