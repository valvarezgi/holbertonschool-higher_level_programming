#!/usr/bin/python3
from magic_calculation(a, b) import add, sub

if a < b:
    c = (a + b)
    for i in range(4, 6):
        c = add(c, i)
    return c
else:
    return sub(a, b)