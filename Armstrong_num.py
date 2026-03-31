# Find common elements without set

def common_elements(l1, l2):
    result = []
    for i in l1:
        if i in l2 and i not in result:
            result.append(i)
    return result


# Input
l1 = list(map(int, input("Enter list1: ").split()))
l2 = list(map(int, input("Enter list2: ").split()))

# Output
print("Common elements:", common_elements(l1, l2))