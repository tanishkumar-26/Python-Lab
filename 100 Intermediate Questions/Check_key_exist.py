n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

check_key = input()

if check_key in d:
    print("Key Exists")
else:
    print("Key Not Found")