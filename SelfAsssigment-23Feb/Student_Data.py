students = {
    101: ("Rahul", "Delhi"),
    102: ("Aman", "Mumbai")
}

for roll, data in students.items():
    print(f"Roll {roll}: Name={data[0]}, City={data[1]}")