# def f(level):
#     # Print recursion level
#     print("Recursion call, level", level)
#     # If we haven't reached level 10...
#     if level < 10:
#         # Call this function again,
#         # adding one to the level
#         f(level + 1)
#
#
# # Start recursive call at level 1
# f(1)


# This program calculates the factorial
# WITHOUT using recursion
# def factorial_nonrecursive(n):
#     answer = 1
#     for i in range(2, n+1):
#         answer = answer * i
#     return answer
#
#
# # This program calculates the factorial using recursion
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursive(n-1)


def f(n):
    if n == 1:
        return 6
    elif n > 1:
        return 0.5 * f(n - 1) + 4


for n in range(1, 11):
    print('n =', f(n), 'a =', n)
print()


def f_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return f_2(n - 1) + f_2(n - 2)


for n in range(1, 11):
    print('n =', f_2(n), 'a =', n)
