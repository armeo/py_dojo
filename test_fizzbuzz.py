from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_input_1_should_return_1(self):
        self.assertEqual('1', self.fizz_buzz.print_string(1))

    def test_input_2_should_return_2(self):
        self.assertEqual('2', self.fizz_buzz.print_string(2))

    def test_input_3_should_return_Fizz(self):
        self.assertEqual('Fizz', self.fizz_buzz.print_string(3))

    def test_input_6_should_return_Fizz(self):
        self.assertEqual('Fizz', self.fizz_buzz.print_string(6))

    def test_input_5_should_return_Buzz(self):
        self.assertEqual('Buzz', self.fizz_buzz.print_string(5))

    def test_input_10_should_return_Buzz(self):
        self.assertEqual('Buzz', self.fizz_buzz.print_string(10))

    def test_input_15_should_return_FizzBuzz(self):
        self.assertEqual('FizzBuzz', self.fizz_buzz.print_string(15))

    def test_input_30_should_return_FizzBuzz(self):
        self.assertEqual('FizzBuzz', self.fizz_buzz.print_string(30))
