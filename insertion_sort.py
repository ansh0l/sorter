#!/usr/bin/env python

import sys

class Node(object):

    def __init__(self, num, next=None):
        assert type(num) == int and (type(next) == Node or not next)
        self.num = num
        self.next = next

filename = sys.argv[1] if len(sys.argv) > 1 else "output.txt"

def insert(start_node, num):
    node = Node(num)
    start = start_node
    if start_node.num > num:
        node.next = start_node
        return node
    else:
        while start_node.num <= num:
            if start_node.next and start_node.next.num <= num:
                continue
            else:
                node.next = start_node.next
                start_node.next = node
                break
            start_node = start_node.next
        return start

with open(filename, "r") as f:
    numbers = [int(i) for i in f.read().split()][:1000]
    print len(numbers)
    start = Node(numbers[0])
    for num in numbers[1:]:
        start = insert(start, num)
    while start:
        print start.num
        start = start.next


