#!/usr/bin/env python
"""
Sample code to sort numbers using Merge sort
 --> http://en.wikipedia.org/wiki/Merge_sort
"""

import sys

def merge(list1, list2):
    """
    Merge two sorted sub-lists into a single list.
    The base case is that each of these lists have 1 elements
    """
    result = []
    len1, len2 = len(list1), len(list2)
    i, j = 0, 0
    while i < len1 or j < len2:
        if i == len1:
            result += list2[j:]
            break
        elif j == len2:
            result += list1[i:]
            break
        else:
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
    return result

def merge_sort(numbers):
    """
    Apply merge sort on a list of numbers
    This is done by recursively applying merge to sorted sub-arrays
    """
    mid = len(numbers)/2
    # mid will be 0 if length was 1
    if mid:
        return merge(merge_sort(numbers[:mid]), merge_sort(numbers[mid:]))
    else: 
        return numbers

# pylint: disable=C0103
if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.1000000.txt"
    with open(filename, "r") as f:
        numbers = [int(num) for num in f.read().split()]

    for num in numbers:
        print num

    numbers = merge_sort(numbers)

    print ""
    for num in numbers:
        print num
