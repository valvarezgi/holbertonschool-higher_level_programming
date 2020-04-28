#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for i in str:
        if n:
            new_string += i
        n -= 1
    return new_string
