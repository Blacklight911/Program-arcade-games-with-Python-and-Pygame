"""Lesson 17"""

# my_list = [15, 57, 14, 22, 72, 79, 26, 56, 42, 40]
#
# temp = my_list[2]
# my_list[2] = my_list[0]
# my_list[0] = temp
#
# print(my_list)


# Selection sort
def selection_sort(list_name):
    for current_position in range(len(list_name)):
        minimum_pos = current_position
        for scan_pos in range(current_position + 1, len(list_name)):
            if list_name[scan_pos] < list_name[minimum_pos]:
                minimum_pos = scan_pos

        if minimum_pos == current_position:
            continue
        else:
            temp = list_name[minimum_pos]
            list_name[minimum_pos] = list_name[current_position]
            list_name[current_position] = temp


# Insertion sort
def insertion_sort(list_name):
    for key_pos in (1, len(list_name)):
        key_value = list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (list_name[scan_pos] > key_value):
            list_name[scan_pos + 1] = list_name[scan_pos]
            scan_pos = scan_pos - 1
            list_name[scan_pos + 1] = key_value

