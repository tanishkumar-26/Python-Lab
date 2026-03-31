# Student name as key, marks tuple as value
students = {
    "Rahul": (85, 90, 78),
    "Aman": (88, 76, 92)
}

for name, marks in students.items():
    print(f"{name} ka total = {sum(marks)}")