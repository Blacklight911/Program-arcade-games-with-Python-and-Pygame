"""
Lesson 15 is telling about linear and binary search
"""
# name_list = []
#
# with open('example_sorted_names.txt', 'r', encoding='utf8') as file:
#     for line in file:
#         line.read()
#         name_list.append(line)
#     file.close()
#
#
# print(name_list)
#
#
# # Linear search
# def linear_search(array, item):
#     i = 0
#     while i < len(array) and array[i] != item:
#         i += 1
#         if i == len(array):
#             return -1
#         else:
#             return i
# search_name = 'Sara'
#
# # Linear search 'for'.
# for i in range(len(name_list)):
#     if name_list[i] == search_name:
#         print(search_name, 'Находится в списке на позиции: ', i+1)
#     if i == len(name_list) - 1:
#         print(search_name, 'Не найдено.')


#
#
# FIND_HERO = 'Wolf Edgar '
# print(linear_search(name_list, FIND_HERO))
#
#
# # Binary Search
# def binary_search(array, find):
#     lower_bound = 0
#     upper_bound = len(array) - 1
#     found = False
#     while lower_bound < upper_bound and found == False:
#         middle_pos = (lower_bound + upper_bound) / 2
#         if array[middle_pos] < find:
#             lower_bound = middle_pos + 1
#         elif array[middle_pos] > find:
#             upper_bound = middle_pos
#         else:
#             found = True
#     if found:
#         print('Имя находится в ячейке', middle_pos)
#     else:
#         print('Имя не найдено а списке')
#
# binary_search(name_list, find)

# Бинарный поиск
name_list = []
file = open('example_sorted_names.txt')
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()
print(name_list)
desired_element = 'Alex Alvarez'
lower_bound = 0
upper_bound = len(name_list)
found = False
while lower_bound < upper_bound and found is False:
    middle_pos = int((lower_bound + upper_bound) / 2)
    if name_list[middle_pos] > desired_element:
        lower_bound = middle_pos + 1
    elif name_list[middle_pos] < desired_element:
        upper_bound = middle_pos
    else:
        found = True

if found:
    print("Имя находится в ячейке", middle_pos + 1)
else:
    print("Имя не было найдено в списке.")
