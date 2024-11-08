import unittest
from unittest import TestCase
import runner


class RunnerTest(TestCase):
    def test_walk(self):
        test_walk = runner.Runner('Гуляем')
        for i in range(1, 11):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    def test_run(self):
        test_run = runner.Runner('Бежим')
        for i in range(1, 11):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    def test_challenge(self):
        test_walk = runner.Runner('Первый')
        test_run = runner.Runner('Второй')
        for i in range(1, 11):
            test_walk.walk()
            test_run.run()
        self.assertNotEqual(test_run.distance, test_walk.distance)


if __name__ == '__main__':
    unittest.main()
