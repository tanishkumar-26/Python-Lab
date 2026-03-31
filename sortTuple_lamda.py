def sort_by_marks(data):
    return sorted(data, key=lambda x: x[1])


data = [("A", 50), ("B", 30), ("C", 40)]
print("Sorted list:", sort_by_marks(data))