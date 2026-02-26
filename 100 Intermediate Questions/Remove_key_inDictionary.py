n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

remove_key = input()

if remove_key in d:
    del d[remove_key]

for key in d:
    print(key, d[key])