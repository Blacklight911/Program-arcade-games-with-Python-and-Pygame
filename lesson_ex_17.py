"""Lesson 17"""
import numpy as np
my_list = [15, 57, 14, 22, 72, 79, 26, 56, 42, 40]


# Selection sort
def selection_sort(list_name):
    for cur_pos in range(len(list_name)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(list_name)):
            if list_name[scan_pos] < list_name[min_pos]:
                min_pos = scan_pos
        temp = list_name[min_pos]
        list_name[min_pos] = list_name[cur_pos]
        list_name[cur_pos] = temp
    return list_name


# Insertion sort
def insertion_sort(list_name):
    for key_pos in (1, len(list_name)):
        key_value = list[key_pos]
        scan_pos = key_pos - 1
        while scan_pos >= 0 and list_name[scan_pos] > key_value:
            list_name[scan_pos + 1] = list_name[scan_pos]
            scan_pos = scan_pos - 1
            list_name[scan_pos + 1] = key_value


# Tests
for _ in range(10):
    print('*', end='')

print()
print()
for i in range(10):
    for j in range(10):
        print('*', end='')
    print()

arr = [0] * 100


def my_lovely_num(num):
    print(num)

my_lovely_num(7)


def average(a, b, c):
    return (a + b + c) // 3


print(average(5, 3, 7))

class Ball():
    pass