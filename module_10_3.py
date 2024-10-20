'''Задача "Банковские операции"'''
import threading
from threading import Thread, Lock

import random
import time


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):

        for i in range(20):

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            transaction_plus = random.randint(50, 500)

            self.balance += transaction_plus

            print(f'Пополнение {transaction_plus}, Баланс: {self.balance}')
            time.sleep(0.002)


    # 2 Снятие"
    def take(self):
        for i in range(20):
            transaction_minus = random.randint(20, 600)
            print(f'Запрос на {transaction_minus}')
            if self.balance >= transaction_minus:
                self.balance -= transaction_minus
                print(f'Снятие: {transaction_minus}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.002)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')


