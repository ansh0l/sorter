#!/usr/bin/env python

import sys
import random

low, high = 0, 10**6
output = sys.argv[1] if len(sys.argv) > 1 else "output.txt"

with open(output, "w") as f:
    elements = []
    for i in range(low, high):
        elements.append(random.randint(low, high))
    if len(sys.argv) == 3 and sys.argv[2].lower() != "reps=true":
        elements = set(elements)
    f.write(' '.join(str(i) for i in elements))

