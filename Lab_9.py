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
