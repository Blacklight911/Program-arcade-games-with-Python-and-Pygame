# def phrase_count(phrase, count):
#     for i in range(1, count+1):
#         print(phrase, i)
#
#
# phrase_count('Hello', 5)


# def square(n):
#     return n ** 2
#
#
# print(square(4))


# def centrifugal_force(r, w, m):
#     return m * r * (w ** 2)
#
#
# radius = int(input('enter radius: '))
# angular_velocity = int(input('enter angular velocity: '))
# mass = int(input('enter mass: '))
# print(centrifugal_force(radius, angular_velocity, mass))


def list_as_parameter(mylist):
    for item in mylist:
        print(item)


my_list = [10, 5, 15, 25]
list_as_parameter(my_list)
