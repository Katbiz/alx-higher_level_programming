#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = abs(number)%10

print_message = ("Last digit of" + " " + number + " is " + lastdigit)

if lastdigit > 5:
    print(print_message + " and is greater than 5")

elif lastdigit == 0:
    print(print_message + " and is 0")

else:
    print(print_message + " and is less than 6 and not 0\n")
