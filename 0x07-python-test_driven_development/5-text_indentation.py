#!/usr/bin/python3
"""
function that prints a text with 2
new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ This function splits texts adding newlines when some separators are found"""
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    total = len(text)
    while i < total:
        if text[0] == ' ':
            pass
        if text[i] == '.' or text[i] == ':' or text[i] == "?":
            print("{}{}".format(text[i],'\n'))
            i += 2
        print("{}".format(text[i]), end="")
        i += 1
        if text[total -1] == ' ':
            pass
