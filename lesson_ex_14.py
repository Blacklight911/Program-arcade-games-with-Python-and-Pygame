import random


class Monster:
    """Bad monster grr"""
    type = 'Monster'
    hit_points = 100

    def monster_print(self):
        print('Monster', self.type, 'has', self.hit_points, 'hit points')


class Orc(Monster):
    def __init__(self):
        self.type = 'Orc'
        self.hit_points = random.randint(15, 30)


class Goblin(Monster):
    def __init__(self):
        self.type = 'Goblin'
        self.hit_points = random.randint(5, 10)


monster_list = []
for monster in range(2):
    monster_orc = Orc()
    monster_list.append(monster_orc)

for monster in range(3):
    monster_goblin = Goblin()
    monster_list.append(monster_goblin)

for monster in monster_list:
    monster.monster_print()
