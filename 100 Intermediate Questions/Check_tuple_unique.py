t = tuple(map(int, input().split()))

if len(t) == len(set(t)):
    print("Unique")
else:
    print("Not Unique")