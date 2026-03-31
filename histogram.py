# Pie chart

import matplotlib.pyplot as plt

def pie_chart(data, labels):
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.show()


# Input
data = [30,40,20,10]
labels = ['A','B','C','D']

# Output
print("Displaying pie chart...")
pie_chart(data, labels)