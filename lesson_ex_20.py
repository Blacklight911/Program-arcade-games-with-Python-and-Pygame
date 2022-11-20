import random
from functools import lru_cache


# for i in range(10):
#     x = random.randrange(20)
#     print(x)

# print()
#
# for i in range(10):
#     x = random.randrange(20)
#     print(f"{i:3}")
#
# print()
#
# for i in range(10):
#     x = random.randrange(100000)
#     print(f"{x:6,}")

# print()

# for i in range(10):
#     x = random.randrange(1000, 100000)
#     print(f"{x:2,}")
#
# print()

# x = 5
# y = 66
# z = 777
# print(f"A - {x} B - {y} C - {z}")
#
# print()

# x = 5
# y = 66
# z = 777
# print(f"C - '{z:3}' A - '{x:1}' B - '{y:2}' C again - '{z:3}'")
#
# print()
#
# my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
#     print(my_fruit[i], "are", my_calories[i], "calories.")
#
# print()
#
# my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
#     print(f"{my_fruit[i]:7} are {my_calories[i]:3} calories.")
#
# print()
# my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
#     print(f"{my_fruit[i]:>7} are {my_calories[i]:<3} calories.")
#
# print()

# for hours in range(1, 13):
#     for minutes in range(0, 60):
#         print(f"Time {hours:02}:{minutes:02}")
#
# print()
#
# score = 41237
# highscore = 1023407
#
# print(f"Очки:{score:12,}")
# print(f"Рекорд:{highscore:10,}")
#
# print()
#
# for i in range(1, 21):
#     print(f'  1/{i:<2} = {1 / i:.3}')
#
#

# This decorator uses LRU cache for speed up the process maximum Fibonacci number is 501
@lru_cache()
def fibonacci_r(num):
    """Standard Fibonacci with recursion, low speed with cycle"""
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci_r(num - 1) + fibonacci_r(num - 2)


for i in range(1, 36):
    print(f'{i:>2} - {fibonacci_r(i):>7}')
