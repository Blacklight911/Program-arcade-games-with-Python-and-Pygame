for rows in range(1, 10):
    for i in range(rows, 10):
        print(' ', end=' ')
    for i in range(1, rows):
        print(i, end=' ')
    for i in range(rows, 0, -1):
        print(i, end=' ')
    print()
for rows in range(8, 0, -1):
    for i in range(rows, 10):
        print(' ', end=' ')
    for i in range(1, rows):
        print(i, end=' ')
    for i in range(rows, 0, -1):
        print(i, end=' ')
    print()
