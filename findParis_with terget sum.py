# Swap dictionary

def swap_dict(d):
    return {v: k for k, v in d.items()}


# Input
d = {'a':1, 'b':2, 'c':3}

# Output
print("Swapped dictionary:", swap_dict(d))