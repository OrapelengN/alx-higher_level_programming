#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle, or an empty
        list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
