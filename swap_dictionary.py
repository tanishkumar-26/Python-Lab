def swap_dict(d):
    swapped = {}
    for k, v in d.items():
        swapped[v] = k
    return swapped


d = {'a':1, 'b':2, 'c':3}
print("Swapped dictionary:", swap_dict(d))