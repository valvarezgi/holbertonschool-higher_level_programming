#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = len(argv)
    if counter == 1:
        print("0 arguments.")
    elif counter == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(counter - 1))
        num = 1
        for i in range(1, counter):
            print("{:d}: {:s}".format(num, argv[i]))
            num += 1
