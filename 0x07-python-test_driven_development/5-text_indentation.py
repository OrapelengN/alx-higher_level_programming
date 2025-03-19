#!/usr/bin/python3
# 5-text_indentation.py
"""
This module defines a function for printing text with proper indentation.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1  # Skip spaces after punctuation
            continue
        i += 1

    print(result, end="")  # Ensures no leading/trailing spaces in output
