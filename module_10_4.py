
from threading import Thread
import queue
from time import sleep
from random import randint

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']


class Table:
    number = None
    def __init__(self, number):
        self.number = number
        self.guest = None
tables = [Table(number) for number in range(1, 6)]

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        expect = randint(3, 10)
        sleep(expect)
guests = [Guest(name) for name in guests_names]

class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables


    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None: #стол свободен
                    guest.start() #гости пошли
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or (table.guest is not None for table in self.tables):#пока очередь не пуста и гость сидит
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:# если очередь непуста и есть свободный стол
                    table.guest = self.queue.get() #приглашаем гостя из очереди
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

cafe = Cafe(*tables) # Заполнение кафе столами
cafe.guest_arrival(*guests) # Приём гостей
cafe.discuss_guests() # Обслужмвание гостей
