#!/usr/bin/python3
""" prints a text with 2 new lines after a . or ?
"""


def text_indentation(text):
    """text_indentation

    Args:
        text (str): text to indent

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        new_text = text.replace(".", ".\n\n")
        new_text = new_text.replace(":", ":\n\n")
        new_text = new_text.replace("?", "?\n\n")
        while "\n\n " in new_text:
            new_text = new_text.replace("\n\n ", "\n\n")
        print(new_text, end="")
