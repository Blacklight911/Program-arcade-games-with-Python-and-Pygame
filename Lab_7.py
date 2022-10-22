"""
Adventure in dungeon
"""
done = False
current_room = 0
next_room = 0

# Initialising rooms
armory = ['You are in the armory, There is the passage to the east', None, 1, None, None]
west_hall = ['Dusty castle room. Passages lead to the north and east and west.', 5, 2, None, 0]
south_hall = ['Dusty castle room with a torch lit. Passages lead to the east and west', None, 3, None, 1]
dining_room = ['The dining room. Looks like passages to the east and west', None, 4, None, 2]
kitchen = ['The kitchen. Passages to the west', None, None, None, 3]
bed_room_1 = ['Ded room 1. Passages going to north, east, west', 8, 6, 1, None]
nort_hall = ['Torch lit hallway. The way going to, east and west ', None, 7, None, 5]
bed_room_2 = ['Bed room 2. A window, overlooks the castle courtyard, only two ways here, north, west', 9, None, None, 6]
balcony_1 = ["balcony 1. Don't jump out, one way here is south", None, None, 5, None]
balcony_2 = ['balcony 2. Good view of the garden below, one way is south', None, None, 7, None]

room_list = [armory, west_hall, south_hall, dining_room, kitchen, bed_room_1, nort_hall,
             bed_room_2, balcony_1, balcony_2]

# ----------- Main Loop -------------
while not done:
    print(room_list[current_room][0])
    print()
    user_input = input('What direction? ')
    print()
    if user_input.lower() == 'n' or user_input.lower() == 'north':
        next_room = room_list[current_room][1]
        if next_room is None:
            print("Can't go this way.")
            print()
        else:
            current_room = next_room

    elif user_input.lower() == 'e' or user_input.lower() == 'east':
        next_room = room_list[current_room][2]
        if next_room is None:
            print("Can't go this way.")
            print()
        else:
            current_room = next_room

    elif user_input.lower() == 's' or user_input.lower() == 'south':
        next_room = room_list[current_room][3]
        if next_room is None:
            print("Can't go this way.")
            print()
        else:
            current_room = next_room

    elif user_input.lower() == 'w' or user_input.lower() == 'west':
        next_room = room_list[current_room][4]
        if next_room is None:
            print("Can't go this way.")
            print()
        else:
            current_room = next_room
