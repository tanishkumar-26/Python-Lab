def unique_elements(lst):
    return list(set(lst))

nums = list(map(int, input().split()))
result = unique_elements(nums)

print(*result)