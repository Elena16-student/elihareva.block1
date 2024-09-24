
class Figure:
    sides_count = 0

    def __init__(self, color: [int, int, int], side):  # палитра и стороны
        self.__color = color
        self.__side = list(side)
        self.filled = True  # принята палитра (rgb), фигура закрашена

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, side):
        for i in side:
            if i > 0 and isinstance(i, int):
                return True
            else:
                return False



    def set_sides(self, *side):
        if self.__is_valid_sides(side):
            self.__side = list(side)

    def get_sides(self):
        return self.__side
        sides_count = int
        if len(*side) != sides_count:
            return
        # def __len__(self):
    #     sum = 0
    #     for i in self.__side:
    #         sum += i
    #     return sum

    def __len__(self):
        return sum(self.__side)
        #return self.__side * self.sides_count

class Circle(Figure):
    sides_count = 1
    __radius = None

    def __init__(self, color: [int, int, int], *side):
        super().__init__(color, side)

    def set_radius(self):
        self.__radius = self.__len__() / (2 * 3.14)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: [int, int, int], *side):
        super().__init__(color, side)

    def get_square(self):
        side = self.get_sides()
        #pp = (side[0] + side[1] + side[2]) / 2
        pp = (sum(side[0:3])) / 2
        #print(pp)
        return (pp * (pp - side[0]) * (pp - side[1]) * (pp - side[2]) ** 0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: [int, int, int], *side):
        if len(side) != 1:
            side = [1]
        super().__init__(color, side)

    def set_sides(self, *side):
        side = side * 12
        if len(side) == 1:
            super().set_sides(side)

    def get_volume(self):
        return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 16)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 8)
triangle1 = Triangle((200, 100, 100), 8, 6, 10)

# Проверка на изменение цветов:
circle1.set_color(360, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(55, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(47, 75, 65)  # Не изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)# Не изменится
cube1.set_sides(5)

triangle1.set_sides(5, 6, 8)
print(cube1.get_sides())
circle1.set_sides(11)  # Изменится
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(len(cube1))

# Проверка объёма (куба):
print(cube1.get_volume())
# площадь треугольника
print(triangle1.get_square())
# площадь круга
print(circle1.get_square())


