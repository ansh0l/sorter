#!/usr/bin/env python
"""
Sample code to sort numbers using Bubble sort
 --> http://en.wikipedia.org/wiki/Bubble_sort
"""

import sys

class Node(object):
    """Individual Node class for each node in a linked list"""

    def __init__(self, num, next=None, prev=None):
        assert type(num) == int and (not next or type(next) == Node
            ) and (not prev or type(prev) == Node)
        self.num = num
        self.next = next
        self.prev = prev

def bubble_sort(start):
    """bubble sort the values"""
    change = 0
    original_start = start
    import pdb; pdb.set_trace()
    while start.next:
        if start.next.num < start.num:
            if not start.prev:
                original_start = start.next
            start.next, start.next.prev = start.next.next, start.prev
            change += 1
        start = start.next
    return change, original_start

# pylint: disable-msg=C0103
if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]
    start = curr = prev = None

    for idx, num in enumerate(numbers):
        if idx == 0:
            start = curr = prev = Node(num)
        else:
            curr = Node(num, prev=prev)
            prev.next = curr
            prev = curr
    change = True
    while change:
        change, start = bubble_sort(start)
    while start:
        print start.num
        start = start.next

