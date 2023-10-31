#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str1 = "Last digit of"
str2 = "and is less than 6 and not 0"
if last_digit > 5 and number > 0:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit < 6 and last_digit != 0 and number > 0:
    print("{} {} is {} {}".format(str1, number, last_digit, str2))
elif last_digit < 6 and last_digit != 0 and number < 0:
    print("{} {} is {} and is less than 6 and not 0".format(str1, number, -last_digit))
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
