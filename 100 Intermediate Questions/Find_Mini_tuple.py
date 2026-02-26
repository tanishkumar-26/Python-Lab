t = tuple(map(int, input().split()))

minimum = t[0]

for num in t:
    if num < minimum:
        minimum = num

print(minimum)