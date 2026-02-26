nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0

print(*nums)