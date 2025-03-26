#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to insert after the found line.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new_lines)
