class House:
    houses_history = []
    '''История строительства'''

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    #def __str__(self):
        #return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        #return self.name
    def __del__(self):
        print(f'{self.name} снесён, но остается в истории')

gh_1 = House('ЖК Зеленодолье', 9)
print(House.houses_history)
gh_2 = House('ЖК Ромашков луг', 7)
print(House.houses_history)
gh_3 = House('ЖК Дубки', 20)
print(House.houses_history)
del gh_3
gh_4 = House('ЖК Березка', 15)
print(House.houses_history)

