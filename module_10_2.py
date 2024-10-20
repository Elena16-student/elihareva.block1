'''"За честь и отвагу!"'''
from threading import Thread
from time import sleep

class Knight(Thread):


    def __init__(self, name:str, power:int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.days = 0
        self.arms = 180 # воинов противника
        while self.arms > 0: # пока жив хоть один враг
            sleep(1)
            print(f'{self.name} сражается {self.days} дней, осталось {self.arms} воинов.')
            self.days += 1
            self.arms = self.arms - self.power # количество недобитых врагов по итогу дня
        print(f'{self.name} одержал победу спустя {self.days} дней(я)!')

knight1 = Knight('Sir Lancelot', 50)
knight2 = Knight('Sir Galahad', 60)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Враги разбиты!')