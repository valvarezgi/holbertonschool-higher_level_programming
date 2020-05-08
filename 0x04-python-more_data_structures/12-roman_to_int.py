#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0

    for element in range(0, len(roman_string)):
        if element == len(roman_string) - 1:
            integer += values[roman_string[element]]
        elif values[roman_string[element]] >= values[roman_string[element + 1]]:
            integer += values[roman_string[element]]
        else:
            integer -= values[roman_string[element]]
    return integer
