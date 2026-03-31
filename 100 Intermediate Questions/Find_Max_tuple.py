t = tuple(map(int, input().split()))

maximum = t[0]

for num in t:
    if num > maximum:
        maximum = num

print(maximum)