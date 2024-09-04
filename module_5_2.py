class House:
    '''ЖК и их характеристики'''


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует.")

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


gh_1 = House('ЖК Зеленодолье', 6)
print(str(gh_1))
print(len(gh_1))
gh_1.go_to(6)

gh_2 = House('ЖК Ромашков луг', 21)
print(str(gh_2))
print(len(gh_2))
gh_2.go_to(26)