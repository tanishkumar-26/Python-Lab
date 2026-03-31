# Remove duplicates

def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


# Input
arr = list(map(int, input("Enter numbers: ").split()))

# Output
print("List without duplicates:", remove_duplicates(arr))