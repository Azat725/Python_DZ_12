def binary_search(array: list, target: int):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
    return -1


def get_union(array: list):
    result = set()
    
    for lst in array:
        result.update(lst)
    return list(result)


array = [
    [1, 2, 3, 5],
    [2, 3, 4, 5],
    [3, 4, 5, 6], 
    [4, 5, 6, 7]
]

value_to_find = 5
sort_ascending = True
unique_elements = get_union(array)
index = binary_search(unique_elements, value_to_find)

if sort_ascending:
    unique_elements.sort()
else:
    unique_elements.sort(reverse=True)
    
print(f"Отсортированный список -> {unique_elements}")
if index == -1:
    print(f"Число не найдено")
else:
    print(f"Число -> {value_to_find} найдено на позиции {index}")
    