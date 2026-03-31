# Flatten nested list

def flatten_list(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result


# Input
nested = [1,[2,3],[4,[5,6]]]

# Output
print("Flattened list:", flatten_list(nested))