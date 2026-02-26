def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

nums = list(map(int, input().split()))
print(second_largest(nums))