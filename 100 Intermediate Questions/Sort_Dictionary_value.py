n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

sorted_items = sorted(d.items(), key=lambda x: x[1])

for key, value in sorted_items:
    print(key, value)