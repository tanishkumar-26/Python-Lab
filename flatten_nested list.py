def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


nested = [1, [2, 3], [4, [5, 6]]]
print("Flattened list:", flatten_list(nested))