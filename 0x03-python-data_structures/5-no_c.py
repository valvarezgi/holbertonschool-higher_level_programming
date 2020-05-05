#!/usr/bin/python3
def no_c(my_string):
    str_to_list = list(my_string)
    [str_to_list.remove(i) for i in str_to_list if i is "c" or i is "C"]
    new_string = "".join(str_to_list)
    return new_string
