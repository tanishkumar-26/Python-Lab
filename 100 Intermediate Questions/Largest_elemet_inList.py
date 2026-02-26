def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

nums = list(map(int, input().split()))
print(find_largest(nums))