#!/usr/bin/env python
"""
Sample code to sort numbers using Selection sort
 --> http://en.wikipedia.org/wiki/Selection_sort
"""

import sys

def selection_sort(numbers):
    pass

if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]
