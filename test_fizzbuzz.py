from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def test_input_1_should_return_1(self):
        fizz_buzz = FizzBuzz()
        actual = fizz_buzz.print_string(1)
        self.assertEqual('1', actual)

    def test_input_2_should_return_2(self):
        fizz_buzz = FizzBuzz()
        actual = fizz_buzz.print_string(2)
        self.assertEqual('2', actual)
