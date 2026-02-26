n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

for key in sorted(d):
    print(key, d[key])