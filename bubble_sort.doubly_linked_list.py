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
    """
    bubble sort the values
    If nodes are in order     |1| -> |2| -> |3| -> |4|,
        and |2| > |3|,
        then the new order is |1| -> |3| -> |2| -> |4|
    """
    change = 0
    current = start
    while current.next:
        if current.next.num < current.num:
            node1, node2, node3 = current.prev, current, current.next
            node4 = current.next.next if current.next.next else None
            if node1:
                node1.next = node3
            else:
                start = node3
            if node4:
                node4.prev = node2
            node2.prev = node3
            node2.next = node4
            node3.prev = node1
            node3.next = node2
            change += 1
        else:
            current = current.next
    return change, start

# pylint: disable=C0103
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

