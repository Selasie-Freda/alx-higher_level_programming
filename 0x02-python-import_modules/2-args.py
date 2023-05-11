#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len == 2:
        print("1 argument:")
        print("{:d}: {}".format(1, sys.argv[1]))
    elif arg_len > 2:
        print("{:d} arguments:".format(arg_len - 1))
        del sys.argv[0]
        for index, argv in enumerate(sys.argv):
            print("{:d}: {}".format(index + 1, argv))
