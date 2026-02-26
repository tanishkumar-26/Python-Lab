nums = list(map(int, input().split()))

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")