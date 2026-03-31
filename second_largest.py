# Find second largest element without using sort()

def find_second_largest(arr):
    if len(arr) < 2:
        return "List should have at least 2 elements"

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element"
    
    return second_largest


# Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Output
result = find_second_largest(numbers)
print("Second largest element is:", result)