n1 = int(input())
dict1 = {}

for i in range(n1):
    key = input()
    value = int(input())
    dict1[key] = value

n2 = int(input())
dict2 = {}

for i in range(n2):
    key = input()
    value = int(input())
    dict2[key] = value

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

for key in merged:
    print(key, merged[key])