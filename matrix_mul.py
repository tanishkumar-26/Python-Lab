# Normalize array

import numpy as np

def normalize(arr):
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))


# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Output
print("Normalized array:", normalize(arr))