# Задача "Мифическое наследование":
# Необходимо написать 3 класса:
# Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
# x_distance = 0 - пройденный путь.
# sound = 'Frrr' - звук, который издаёт лошадь.
# И методами:
# run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.
#
# Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
# y_distance = 0 - высота полёта
# sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
# И методами:
# fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.
#
# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
# Также обладает методами:
# move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
# get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
# voice - который печатает значение унаследованного атрибута sound.
# Пункты задачи:
# Создайте классы родители: Horse и Eagle с методами из описания.
# Создайте класс наследник Pegasus с методами из описания.
# Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.
#
# Пример результата выполнения программы:
# Пример работы программы:
# p1 = Pegasus()
#
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()
#
# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat

#
# Примечания:
# Будьте внимательней, когда вызываете методы классов родителей в классе наследнике
# при множественном наследовании: при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала
# идёт наследование от Horse, а после от Eagle.

#

 #
#
#     def get_pos(self):
#         print(f'Координаты Пегаса в полете: {self.x_distance}, {self.y_distance}')
#     def voice(self):
#         return f'voice{self.sound}'
#
#
# p1 = Pegasus()
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()


class Horse:

    def __init__(self):
        self.x_distance = 0  #путь
        self.sound = 'Frrr'
        super().__init__()
    def run(self, dx):
        self.x_distance += dx   #продвинулся  на dx

class Eagle:

    def __init__(self):
        self.y_distance = 0 #начало набора высоты
        self.sound_1 = 'I train, eat, sleep and repeat'  #звук орла
    def fly(self, dy):   # поднимается на высоту (на dy)
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy): #полет в двухмерном пространстве
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
       return f'Координаты Пегаса в полете: удаленность {self.x_distance}, высота {self.y_distance}'

    def voice(self):
        print(f'Возгласы: {self.sound_1}, {self.sound}')
        #немного усложним задачу, пусть Пегас поет на все голоса




p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(26, 67)
print(p1.get_pos())

p1.voice()

