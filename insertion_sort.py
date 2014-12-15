#!/usr/bin/env python

import sys

class Node(object):
    """Individual Node class for each node in a linked list"""

    def __init__(self, num, next=None):
        assert type(num) == int and (not next or type(next) == Node)
        self.num = num
        self.next = next

def insert(start_node, num):
    """Inserts elements in a linked list"""

    start = start_node
    if num < start.num:
        return Node(num, start)
    else:
        while start.num <= num:
            if not (start.next and start.next.num <= num):
                start.next = Node(num, start.next)
                break
            start = start.next
        return start_node

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()]
    start = Node(numbers[0])
    for num in numbers[1:]:
        start = insert(start, num)
    while start:
        print start.num
        start = start.next
