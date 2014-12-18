#!/usr/bin/env python
"""
Sample code to sort numbers using Merge sort
 --> http://en.wikipedia.org/wiki/Merge_sort
"""

import sys


def merge(list1, list2):
    result = []
    return result

def merge_sort(numbers):
    mid = len(numbers)/2
    if mid:
        return merge(merge_sort(numbers[:mid]), merge_sort(numbers[mid:]))
    else: # mid will be 0 => length was 1
        return numbers

if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]

    for i in numbers:
        print i

    numbers = merge_sort(numbers)

    print ""
    for i in numbers:
        print i
