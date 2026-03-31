# Two dataset plot

import matplotlib.pyplot as plt

def multi_plot(x, y1, y2):
    plt.plot(x, y1, label="Data1")
    plt.plot(x, y2, label="Data2")
    plt.legend()
    plt.show()


# Input
x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [40,30,20,10]

# Output
print("Displaying combined plot...")
multi_plot(x, y1, y2)