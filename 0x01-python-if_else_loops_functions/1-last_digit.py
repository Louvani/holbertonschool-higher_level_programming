#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    digit = number % 10
elif number < 0:
    digit = number % -10
print('Last digit of {:d} is {:d} '.format(number, digit), end="")
if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
