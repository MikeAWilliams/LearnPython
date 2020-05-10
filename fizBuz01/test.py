import unittest
from fizzBuzz import FizzBuzz

class TestFizBuz(unittest.TestCase):

    def test_one(self):
        self.assertEqual("1", FizzBuzz(1))

    def test_two(self):
        self.assertEqual("2", FizzBuzz(2))

    def test_three(self):
        self.assertEqual("fizz", FizzBuzz(3))

    def test_four(self):
        self.assertEqual("4", FizzBuzz(4))

    def test_five(self):
        self.assertEqual("buzz", FizzBuzz(5))

    def test_six(self):
        self.assertEqual("fizz", FizzBuzz(6))

    def test_nine(self):
        self.assertEqual("fizz", FizzBuzz(9))

    def test_ten(self):
        self.assertEqual("buzz", FizzBuzz(10))

    def test_fifteen(self):
        self.assertEqual("fizzbuzz", FizzBuzz(15))


if __name__ == '__main__':
    unittest.main()