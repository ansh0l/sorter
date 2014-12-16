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
    """bubble sort the values
    If nodes are in order     |1| -> |2| -> |3| -> |4|, 
        and |2| > |3|,
        then the new order is |1| -> |3| -> |2| -> |4|
    """
    change = 0
    current = start
    import pdb; pdb.set_trace()
    try:
        while current.next:
            if current.next.num < current.num:
                n1, n2, n3 = current.prev, current, current.next
                n4 = current.next.next if current.next.next else None
                if n1: n1.next = n3
                else: start = n3
                if n4: n4.prev = n2
                n2.prev = n3
                n2.next = n4
                n3.prev = n1
                n3.next = n2
                change += 1
            else:
                current = current.next
    except Exception as e:
        import pdb; pdb.set_trace()
        print e.message
    return change, start

# pylint: disable-msg=C0103
if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.10000.txt"
    with open(filename, "r") as f:
        numbers = [int(i) for i in f.read().split()][:10]
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
        st = start
        while st:
            print st.num
            st = st.next
        change, start = bubble_sort(start)

