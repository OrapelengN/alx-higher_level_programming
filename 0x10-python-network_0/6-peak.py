#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of integers.

    Returns:
        int: The peak element, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
