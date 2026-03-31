# Extract diagonal

import numpy as np

def diagonal(mat):
    return np.diag(mat)


# Input
mat = np.array([[1,2],[3,4]])

# Output
print("Diagonal elements:", diagonal(mat))