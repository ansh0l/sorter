#!/usr/bin/env python
"""
Sample code to sort numbers using Heap sort
 --> http://en.wikipedia.org/wiki/Heapsort
"""

import sys

def heapify(numbers):
    return numbers

def heap_sort(numbers):
    result = []
    while len(numbers) > 1:
        numbers = heapify(numbers[1:])
        result.append(numbers[0])
    return result

if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(num) for num in f.read().split()]

    for num in numbers:
        print num

    numbers = heap_sort(numbers)

    print ""
    for num in numbers:
        print num
