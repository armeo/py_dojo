class FizzBuzz(object):
    def print_string(self, input):
        fizz_buzz = "Fizz" * (input %3 == 0) + "Buzz" * (input % 5 == 0)
        return fizz_buzz or str(input)
