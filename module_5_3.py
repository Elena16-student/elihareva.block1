class House:

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



    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value:any):
        return self + value

    def __radd__(self, value):
        return self + value


def main():

    gh_1 = House('ЖК Зеленодолье', 9)
    print(str(gh_1))
    print(len(gh_1))
    gh_1.go_to(6)

    gh_2 = House('ЖК Ромашков луг', 7)
    print(str(gh_2))
    print(len(gh_2))
    gh_2.go_to(26)

    print(isinstance(gh_1, int | House))
    print(isinstance(gh_2, int | House))
    print(type(gh_2))

    print(gh_1 == gh_2)  # __eq__

    gh_1 = gh_1 + 10  # __add__
    print(gh_1)

    gh_1 += 10  # __iadd__
    print(gh_1)

    gh_2 = 8 + gh_2  # __radd__
    print(gh_2)

    print(gh_1 > gh_2)  # __gt__
    print(gh_1 >= gh_2)  # __ge__
    print(gh_1 < gh_2)  # __lt__
    print(gh_1 <= gh_2)  # __le__
    print(gh_1 != gh_2)  # __ne__

if __name__ == '__main__':
    main()
