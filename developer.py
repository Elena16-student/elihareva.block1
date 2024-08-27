class House:
    '''ЖК и их характеристики'''


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor: int):

        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range (1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


gh_1 = House('Зеленодолье', 12)
gh_2 = House('Ромашков луг', 14)
gh_1.go_to(8)
gh_2.go_to(23)