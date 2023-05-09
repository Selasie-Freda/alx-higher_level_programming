#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = []
if number > 0 and len(str(number)) >= 2:
    for i in str(number):
        num.append(int(i))
    last_digit = num[-1]

elif number < 0 and len(str(number)) >= 2:
    for i in str(number):
        if i == "-":
            pass
        else:
            x = int(i) * -1
            num.append(x)
    last_digit = num[-1]

elif len(str(number)) <= 1:
    last_digit = number
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of", number, "is", last_digit,
          "and is less than 6 but not 0")
