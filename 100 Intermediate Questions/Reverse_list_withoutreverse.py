def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

nums = list(map(int, input().split()))
print(*reverse_list(nums))