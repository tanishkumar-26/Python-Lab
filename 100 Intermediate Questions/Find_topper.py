n = int(input())

marks = {}

for i in range(n):
    name = input()
    score = int(input())
    marks[name] = score

topper = max(marks, key=marks.get)

print(topper)