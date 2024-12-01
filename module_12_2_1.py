import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:  # согласно списку бегунов
            for participant in self.participants:  # для каждого участника в списке:
                participant.run()                  # выстрел стартового пистлета
                if participant.distance >= self.full_distance:  # если бегун пересек финишную черту
                    finishers[place] = participant  # ключ:значение, где ключ- место, а значение-имя участника
                    place += 1                      # продолжаем забег и смотрим, кто прибежит следующим,
                    self.participants.remove(participant) # когда участник добежал до финиша, удаляем его из списка
        return finishers # возврат результатов в словарик


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.part_1 = Runner('Усейн', 10)
        self.part_2 = Runner('Андрей', 9)
        self.part_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        for result in cls.all_results.values():
            finishers = {}
            for place, runner in result.items():
                finishers[place] = runner.name
            print(finishers)

    def test_run_1(self):
        self.first_tour = Tournament(90, self.part_1, self.part_3 )  # создаем объект класса Забег
        self.all_results = self.first_tour.start() # записываем  в словарь результат место:бегун
        last_runner_name = self.all_results[max(self.all_results.keys())].name # максимальное место - пришел последним
        self.assertTrue(last_runner_name == 'Ник')  # юнит-метод сравнения
        TournamentTest.all_results[1] = self.all_results # записываем рез-ты забега

    def test_run_2(self):
        self.second_tour = Tournament(90, self.part_2, self.part_3 )
        self.all_results = self.second_tour.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.third_tour= Tournament(90, self.part_1, self.part_2, self.part_3 )
        self.all_results = self.third_tour.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()