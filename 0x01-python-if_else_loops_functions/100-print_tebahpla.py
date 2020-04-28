#!/usr/bin/python3
for i in range(122, 96, -1):
    starts_in = 0
    if i % 2:
        starts_in = 32
    print("{:c}".format(i - starts_in), end="")
