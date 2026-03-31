def merge_lists(lst1, lst2):
    merged = lst1 + lst2
    result = []
    for num in merged:
        if num not in result:
            result.append(num)
    return result

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(*merge_lists(list1, list2))