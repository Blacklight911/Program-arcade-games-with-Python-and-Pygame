"""
Area of trapezoid
"""


height = int(input('Введите высоту трапеции: '))
length_top = int(input('Введите длину верхнего основания: '))
length_bottom = int(input('Введите длину нижнего основания: '))

trapezoid_area = 1 / 2 * (length_top + length_bottom) * height

print('Площадь трапеции равна:', trapezoid_area)
