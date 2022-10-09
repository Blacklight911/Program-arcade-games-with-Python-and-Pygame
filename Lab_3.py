"""
Quiz time!
"""

question_1 = int(input('Сколь лет Биллу Гейтсу? '))
count = 0

if question_1 == 66:
    print('Верно!')
    count += 1
else:
    print('Неверно!')
print()

question_2 = int(input('5 * 5 = ? '))

if question_2 == 25:
    print('Верно!')
    count += 1
else:
    print('Неверно!')
print()


question_3 = input('Введите правильный вариант ответа: \n'
                   'Собака \n'
                   'Пума \n'
                   'Гепард \n'
                   'Рысь \n')

if question_3.lower() == 'собака':
    print('Верно!')
    count += 1
else:
    print('Неверно!')
print()

question_4 = int(input('Число дня рожденья Джеки Чана '))

if question_4 == 7:
    print('Верно!')
    count += 1
else:
    print('Неверно!')
print()

question_5 = input('Закончите фразу - Рик и ... ? ')

if question_5 == 'Морти':
    print('Верно')
    count += 1
else:
    print('Неверно!')
print()

print('Ваш результат', count, 'очков')


