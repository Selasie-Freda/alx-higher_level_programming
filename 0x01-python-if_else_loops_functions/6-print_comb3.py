#!/usr/bin/python3
for i in range(0, 10):
    for y in range(0, 10):
        if i == 8 and y == 9:
            print("{:d}{:d}".format(i, y))
        elif i < y:
            print("{:d}{:d}".format(i, y), end=", ")
