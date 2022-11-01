class MyClass:
    name = ''


class YourClass:
    name = ''


black = MyClass()
white = black
print(id(black))
print(id(white))


my_list = [1, 2, 3]
your_list = my_list
my_list.append(5)

print(my_list, id(my_list))
print(your_list, id(your_list))
