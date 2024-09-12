class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name


class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
    def __init__(self, name):
        super().__init__(name)


an_1 = Predator('Яутжа')
an_2 = Mammal('Ягненок')
pl_1 = Flower('Лотос')
pl_2 = Fruit('Манго')

print(an_1.name)
print(pl_1.name)
print(an_2.name)
print(pl_2.name)

print(an_2.alive) # до еды
print(an_1.fed)

an_1.eat(pl_1) #  # пытался есть цветы - не зашли
an_1.eat(pl_2)# поел фруктов и сыт
print(an_1.alive)# выжил?
print(an_1.fed) # накормлен?

an_2.eat(pl_1) # пытался есть цветы - не зашли
an_2.eat(pl_2) # поел фруктов и сыт

print(an_2.alive)
print(an_2.fed)
