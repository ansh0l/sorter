#!/usr/bin/env python
"""
Sample code to sort numbers using Selection sort
 --> http://en.wikipedia.org/wiki/Selection_sort
"""

import sys

def selection_sort(numbers):
    idx, length, min_idx = 0, len(numbers), 0
    for idx in range(length):
        min_idx = length - 1
        for looper in range(idx, length):
            if numbers[looper] < numbers[min_idx]:
                min_idx = looper
        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]
    return numbers

if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]

    for i in numbers:
        print i

    numbers = selection_sort(numbers)

    print ""
    for i in numbers:
        print i
