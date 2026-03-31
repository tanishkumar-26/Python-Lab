keys = input().split()
values = list(map(int, input().split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

for key in d:
    print(key, d[key])