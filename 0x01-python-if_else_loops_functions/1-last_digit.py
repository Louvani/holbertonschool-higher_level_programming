#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
elif number < 0:
    number = number * -1
    last_digit = number % 10
    last_digit = last_digit * -1
    number = number * -1

if last_digit > 5:
    print("Last digit of {:d} is {}"
            " and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {} and is 0".format(number, last_digit))
elif last_digit < 6:
    print("Last digit of {:d} is {}"
            " and is less than 6 and not 0".format(number, last_digit))
