# Histogram

import matplotlib.pyplot as plt
import numpy as np

def histogram(data):
    plt.hist(data)
    plt.show()


# Input
data = np.random.randn(100)

# Output
print("Displaying histogram...")
histogram(data)