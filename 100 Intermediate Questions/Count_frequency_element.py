def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

nums = list(map(int, input().split()))
result = count_frequency(nums)

for key in result:
    print(key, result[key])