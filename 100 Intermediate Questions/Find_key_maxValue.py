n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

max_key = max(d, key=d.get)

print(max_key)