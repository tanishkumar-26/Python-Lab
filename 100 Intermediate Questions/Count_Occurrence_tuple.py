t = tuple(map(int, input().split()))
x = int(input())

count = 0
for num in t:
    if num == x:
        count += 1

print(count)