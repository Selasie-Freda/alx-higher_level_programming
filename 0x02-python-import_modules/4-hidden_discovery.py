#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    num = len(name)
    for i in range(0, num):
        if name[i][1] != "_":
            print("{}".format(name[i]))
