#!/usr/bin/env python
"""
Sample code to sort numbers using Bubble sort
 --> http://en.wikipedia.org/wiki/Bubble_sort
"""

import sys

def bubble_sort(numbers):
    """bubble sort the values"""
    change = True
    while change:
        change = 0
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                change += 1
    return numbers

# pylint: disable=C0103

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]
    numbers = bubble_sort(numbers)
    for number in numbers:
        print number
