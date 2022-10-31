def hello():
    print('Hello')


hello()


def len_of_string(text):
    return len(text)


some_text = 'Say something'
print(len_of_string(some_text))


def print_array(array):
    for item in array:
        print(item)


arr = [1, 2, 3, 5]
print_array(arr)


def sum_array(array):
    sum = 0
    for item in array:
      sum += item
    return sum


my_list = [1, 5, 7]
print(sum_array(my_list))
