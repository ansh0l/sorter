#!/usr/bin/env python

import sys

class Node(object):

    def __init__(self, num, next=None):
        assert type(num) == int and type(next) == Node
        self.num = num
        self.next = next

filename = sys.argv[1] if len(sys.argv) > 1 else "output.txt"

with open(filename, "r") as f:
    numbers = [int(i) for i in f.read().split()]

