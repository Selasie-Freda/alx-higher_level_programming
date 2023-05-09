#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 96 < ord(letter) < 123:
            upper = ord(letter) - 32
        else:
            upper = ord(letter)
        print("{}".format(chr(upper)), end="")
    print("")
