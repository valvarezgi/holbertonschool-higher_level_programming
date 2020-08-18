#!/usr/bin/python3
"""Finds a peak in a list"""


def find_peak(list_of_integers):
    """finds a peak"""
    if list_of_integers:
        return max(list_of_integers)
    return None
