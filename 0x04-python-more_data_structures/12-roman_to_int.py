#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0

    for elem in range(0, len(roman_string)):
        if elem == len(roman_string) - 1:
            integer += values[roman_string[elem]]
        elif values[roman_string[elem]] >= values[roman_string[elem + 1]]:
            integer += values[roman_string[elem]]
        else:
            integer -= values[roman_string[elem]]
    return integer
