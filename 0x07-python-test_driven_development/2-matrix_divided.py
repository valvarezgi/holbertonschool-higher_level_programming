#!/usr/bin/python3
""" Divides a matrix by the number given
"""


def matrix_divided(matrix, div):
    """matrix_divided divides a matrix

    Args:
        matrix (list): list of list of the same length
        div (integer): number to divide eac element

    Raises:
        TypeError: div must be a number, when div is different from integer
        or float
        ZeroDivisionError: division by zero is not allowed
        TypeError: All the lists in the matrix have to be of the same size
        TypeError: Matrix must be a list of list of integers and/or floats

    Returns:
        matrix: matrix of the result
    """
    result = []
    error1 = ("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        lists_i = []
        for element in lists:
            if not isinstance(element, (int, float)):
                raise TypeError(error1)
            else:
                lists_i.append(round(element / div, 2))
        result.append(lists_i)

    return result
