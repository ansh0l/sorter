#!/usr/bin/env python
"""
Sample code to sort numbers using Bogo sort
 --> http://en.wikipedia.org/wiki/Bogosort
"""

import sys
import random

def is_sorted(numbers):
    return all(numbers[i-1] < numbers[i] for i in range(1, len(numbers)))

def bogo_sort(numbers):
    while not is_sorted(numbers):
        idx1, idx2 = random.randint(0, len(numbers) - 1)
        while idx1 == idx2:
            idx2 = random.randint(0, len(numbers) - 1)
        numbers[idx1], numbers[idx2] = numbers[idx2], numbers[idx1]
    return numbers

if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()][:10]

    sorted_numbers = bogo_sort(numbers)
    print numbers, sorted_numbers
