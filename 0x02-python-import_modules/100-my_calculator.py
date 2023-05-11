#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operator = ["+", "-", "*", "/"]
    del sys.argv[0]
    arg_len = len(sys.argv)
    if arg_len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[1] == '+':
        print(sys.argv[0], '+', sys.argv[2], '=', add(int(sys.argv[0]),
              int(sys.argv[2])))
        sys.exit(0)
    elif sys.argv[1] == '-':
        print("{} - {} = {:d}".format(sys.argv[0], sys.argv[2],
              sub(int(sys.argv[0]), int(sys.argv[2]))))
        sys.exit(0)
    elif sys.argv[1] == '*':
        print("{} * {} = {:d}".format(sys.argv[0], sys.argv[2],
              mul(int(sys.argv[0]), int(sys.argv[2]))))
        sys.exit(0)
    elif sys.argv[1] == '/':
        print("{} / {} = {:d}".format(sys.argv[0], sys.argv[2],
              div(int(sys.argv[0]), int(sys.argv[2]))))
        sys.exit(0)

    for i in operator:
        if sys.argv[1] != i:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
