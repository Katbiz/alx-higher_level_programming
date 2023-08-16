#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(str(number) + " is positve.")
elif number < 0:
    print(str(number) + " is negative")
else:
    print(str(number) + "This is zero")
