class Dog:
    age = int()
    name = str()
    weight = float()


my_pet = Dog()
my_pet.age = 7
my_pet.name = 'Dozor'
my_pet.weight = 5


class Person:
    name = ''
    cell_phone = ''
    email = ''


first_man = Person()
first_man.name = 'Antony'
first_man.cell_phone = '89993067788'
first_man.email = 'antony@mail.com'

second_man = Person()
second_man.nane = 'Viktor'
second_man.cell_phone = '89987088877'
second_man.email = 'viktor@mail.com'


class Bird:
    color = ''
    name = ''
    breed = ''


myBird = Bird()
myBird.color = "green"
myBird.name = "Sunny"
myBird.breed = "Sun Conure"


class MyPersonFor2DGame:
    age = 0
    name = ''
    gender = ''
    power = ''


player = MyPersonFor2DGame()
player.age = 22
player.name = 'Alex'
player.gender = 'Male'
player.power = 20


class Dog:
    name = ''
    weight = 0
    age = 0

    def bark(self):
        print('Woof says', self.name)


myDog = Dog()
myDog.name = 'Spot'
myDog.weight = 20
myDog.age = 3


class Cat:
    name = ''
    color = ''
    weight = 0

    def meow(self):
        print(self.name, 'says Meow')


barsik = Cat()
barsik.name = 'Barsik'
barsik.color = 'black'
barsik.weight = 4
barsik.meow()


class Monster:
    name = ''
    health = 0.0

    def decrease_health(self, ammount):
        self.health -= ammount
        if self.health <= 0:
            print(self.name, 'killed')


kaka_demon = Monster()
kaka_demon.name = 'Kaka Demon'
kaka_demon.health = 20

kaka_demon.decrease_health(15)
kaka_demon.decrease_health(5)
