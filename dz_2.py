def linear_search(array: list, target: int):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list3 = [1, 2, 3, 4]
list4 = [7, 6, 5, 4]

union_lists = list1 + list2 + list3 + list4

value_to_find = 5
sort_ascending = True

if sort_ascending == True:
    union_lists.sort()
else:
    union_lists.sort(reverse=True)
    
index = linear_search(union_lists, value_to_find)

print(f"Отсортированный список -> {union_lists}")

if index == -1:
    print("Число не найдено")
else:
    print(f"Число найдено на позиции {index}")