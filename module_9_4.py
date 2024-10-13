from  random import choice

first = 'Роза  упала на лапу Азора'
second = 'Рыба ищет где глубже'

result = list(map(lambda x, y: x == y, first, second))
print(result)

def get_advanced_writer(file_name):

        def write_everything(*data_set):
            with open(file_name, 'w', encoding='UTF-8') as file:
                for i in data_set:
                    file.write(str(i) + '\n')
                    #file.write('\n')
        return write_everything

write = get_advanced_writer('example.txt')
write('Неужели', ['Все', 'это', 'получится', 'число', 10])

class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        word = choice(self.word)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Невероятно', 'В любом случае')
print(first_ball())
print(first_ball())
print(first_ball())
