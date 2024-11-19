import unittest
from unittest import TestCase
import runner


def __init__(self, name):
    self.name = name
    self.distance = 0


def run(self):
    self.distance += 10


def walk(self):
    self.distance += 5


def __str__(self):
    return self.name

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_walk = runner.Runner('Гуляем')
        for i in range(1, 11):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run = runner.Runner('Бежим')
        for i in range(1, 11):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_walk = runner.Runner('Первый')
        test_run = runner.Runner('Второй')
        for i in range(1, 11):
            test_walk.walk()
            test_run.run()
        self.assertNotEqual(test_run.distance, test_walk.distance)

if __name__ == '__main__':
    unittest.main()
