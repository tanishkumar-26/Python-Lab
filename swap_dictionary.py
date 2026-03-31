<<<<<<< HEAD
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
=======
def swap_dict(d):
    swapped = {}
    for k, v in d.items():
        swapped[v] = k
    return swapped


d = {'a':1, 'b':2, 'c':3}
print("Swapped dictionary:", swap_dict(d))
>>>>>>> 2cd8d803fbdaa1272fd8af65f80413fe02d5c278
