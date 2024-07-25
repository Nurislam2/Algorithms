from algorithms import *

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список:", sorted_list)

element_to_search = 25
index = binary_search(sorted_list, element_to_search)

if index != -1:
    print(f"Элемент {element_to_search} найден в индексе: {index}")
else:
    print(f"Элемент {element_to_search} не найден в списке")