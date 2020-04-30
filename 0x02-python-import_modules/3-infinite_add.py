#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

add = 0
if len(argv) == 1:
    add = 0
else:
    for number in range(1, len(argv)):
        add +=int(argv[number])
print("{:d}".format(add))