import random
"""
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives.
"""

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.\n')

done = False

miles = 0
thirst = 0
camel_tiredness = 0
natives_have_traveled = -20
number_of_drinks_in_canteen = 3


while not done:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.\n')

    user_choice = input('Make your choice ! ')

    if user_choice.lower() == 'q':
        done = True
    elif user_choice.lower() == 'e':
        print('Miles traveled: ', miles)
        print('Drinks in canteen: ', number_of_drinks_in_canteen)
        print('The natives are', natives_have_traveled, 'miles behind you \n')
    elif user_choice.lower() == 'd':
        print('You choice stay for the night')
        print('Camel is happy')
        camel_tiredness = 0
        natives_have_traveled += random.randrange(7, 15)
    elif user_choice.lower() == 'c':
        print()
        print('Full speed!!! Go go turbo camel')
        miles += random.randrange(10, 21)
        print('Miles traveled: ', miles)
        print()
        thirst += 1
        camel_tiredness += random.randrange(1, 4)
        natives_have_traveled = random.randrange(7, 15)
    elif user_choice.lower() == 'b':
        print('Moderate speed, keep going')
        miles += random.randrange(5, 13)
        print('Miles traveled: ', miles)
        thirst += 1
        camel_tiredness += 1
        natives_have_traveled = random.randrange(7, 15)
    elif user_choice.lower() == 'a':
        print('Do you want drink from your canteen? Y/N ')
        drink = input()
        if drink.lower() == 'y':
            if number_of_drinks_in_canteen > 0 and thirst > 0:
                number_of_drinks_in_canteen -= 1
                thirst -= 1
                print('You drink from your canteen \n')
            else:
                print("You haven't drinks in your canteen \n")
        elif drink.lower() == 'n':
            print('Gotta go, natives are coming \n')
            natives_have_traveled += random.randint(7, 15)
    if 6 >= thirst > 4:
        print('You want drink!')
    elif thirst > 6 and done is False:
        print('You died of thirst! \n')
        print('Game Over')
        done = True
    if 8 >= camel_tiredness > 5:
        print('Your camel is getting tired\n')
    elif camel_tiredness > 8 and done is False:
        print('Your camel is dead\n')
        print('Game Over')
        done = True
    if natives_have_traveled >= miles:
        done = True
        print('Natives catch you!\n')
        print('Game over')
    if (miles - natives_have_traveled) > 15 and user_choice.lower() != 'e' and done is False:
        print('Natives less than 15 miles behind')
        print('Natives getting close!\n')
    if done is False and miles >= 200:
        print('You won! You across the desert \n')
        done = True
    if done is False and random.random() < 0.2 and user_choice.lower() != 'e':
        print('You find Oasis! Your thirst and camel tiredness restored, also yor canteen refile \n')
        thirst = 0
        camel_tiredness = 0
        number_of_drinks_in_canteen = 3
