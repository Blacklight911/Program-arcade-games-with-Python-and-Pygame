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


class Ball:
    pos_x = 0
    pos_y = 0
    change_x = 2
    change_y = 2

    def update(self):
        self.change_x += self.pos_x
        self.change_y += self.pos_y


my_ball = Ball()
for i in range(10):
    my_ball.update()

my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]

temp = my_list[-3]
my_list[-3] = my_list[-4]
my_list[-4] = temp

my_list = [27, 32, 18, 2, 11, 57, 14, 38, 19, 91]

temp = my_list[0]
my_list[0] = my_list[3]
my_list[3] = temp