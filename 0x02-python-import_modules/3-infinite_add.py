#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for index, arg in enumerate(sys.argv):
        if index == 0:
            continue
        else:
            sum += int(sys.argv[index])
    print(sum)
