class StepValueError(ValueError):
    pass

class  Iterator:

    def __init__(self, start:int, stop:int, step = 1):
        if step == 0:
            raise StepValueError('мы не можем шагать на месте')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        x = self.pointer
        if  (self.step < 0 and x < self.stop) or (self.step > 0 and x > self.stop):
            raise StopIteration
        self.pointer += self.step
        return x
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Так не пойдет, укажите верное значение шага')
    iter2 = Iterator( -7, -14, -1)
    iter3 = Iterator(6, 15,)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 19, 0.5)
    iter6 = Iterator(10, 19)
    iter7 = Iterator(-11, 6, 5)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
    for i in iter6:
        print(i, end=' ')
    print()
    for i in iter7:
        print(i, end=' ')
    print()