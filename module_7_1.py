class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        pozition = str(f"{self.name}, {self.weight}, {self.category}")
        return pozition


class Shop:
    def __init__(self):
        __file_name = 'products.txt'


    def get_products(self):

        __file_name = open('products.txt', 'r')  # открываем products.txt в режиме чтения
        name_poz =__file_name.read()  # считываем список позиций
        __file_name.close()  # закрываем файл
        return name_poz

    def add(self, *products):

        for pozition in products:  # сравниваем продукты в существующем списке
            # и добавляем неорганич. кол-во новых позиций, если их не было
            if str(pozition) not in self.get_products():
                __file_name = open('products.txt', 'a+')  # режим «a+» также открывает файл на чтение и запись,
                # но в отличие от режима «w+», он добавляет данные в конец файла,не удаляя существующие
                __file_name.write(f'{str(pozition)}\n')
                __file_name.close()
            else:
                print(f'Продукт {pozition} уже есть в магазине')


s = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Sugar', 10, 'Groceries')
p5 = Product('Cucumber', 3, 'Vegetables')
p6 = Product('Strawberry', 9, 'Fruit')
p7 = Product('Marshmellow', 2, 'Candy')
p8 = Product('Melon', 4, 'Fruit')
p9 = Product('Rice', 12, 'Groceries')
print(p2)
print(p4)
print(p5)
print(p6)

s.add(p6, p2, p3, p4, p7, p8, p9)
print(s.get_products())
