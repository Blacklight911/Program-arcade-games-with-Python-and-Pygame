import random


def min3(a, b, c):
    if b > a < c:
        return a
    elif a > b < c:
        return b
    elif a > c < b:
        return c
    elif a == b < c:
        return a
    elif a == c < b:
        return a
    elif b == c < a:
        return b
    else:
        return a


print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

print()


def box(h, w):
    for i in range(h):
        for j in range(w):
            print('*', end='')
        print()


box(7, 5)
print()
box(3, 2)
print()
box(3, 10)


def find(list_my, key):
    pass


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

print()


def find(li, key):
    for i in range(len(li)):
        if li[i] == key:
            print('Found', key, 'at position', i)


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)
print()


def create_list(size):
    random_list = []
    for i in range(size):
        random_list.append(random.randrange(1, 6))
    return random_list


my_list = create_list(5)
print(my_list)

print()


def count_list(the_list, num):
    count_number = 0
    for item in the_list:
        if item == num:
            count_number += 1
    return count_number


count = count_list([1, 2, 3, 3, 3, 4, 2, 1], 3)
print(count)

print()


def average_list(array):
    summa = 0
    for i in array:
        summa += i
    return summa // len(array)


avg = average_list([1, 2, 3])
print(avg)
print()

the_big_list = create_list(10000)
print(the_big_list)
count_of_1 = count_list(the_big_list, 1)
count_of_2 = count_list(the_big_list, 2)
count_of_3 = count_list(the_big_list, 3)
count_of_4 = count_list(the_big_list, 4)
count_of_5 = count_list(the_big_list, 5)
print(count_of_1, count_of_2, count_of_3, count_of_4, count_of_5)
print(average_list(the_big_list))
