# Line plot

import matplotlib.pyplot as plt

def line_plot(x, y):
    plt.plot(x, y)
    plt.show()


# Input
x = [1,2,3,4]
y = [10,20,15,25]

# Output
print("Displaying line plot...")
line_plot(x, y)