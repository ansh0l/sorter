#!/usr/bin/env python

import sys
import random

"""
Features:

1. Generate a list of numbers for different sorting algorithms
2. Save them to the user specified file if inputted, else to `output.txt`
3. If the flag reps=True is passed, allow repetition of numbers
4. The numbers generated belong to th range (0, 1000000)

Execution possibilities:

./data_generator.py
./data_generator.py outfile.txt
./data_generator.py outfile.txt reps=True
python data_generator.py
python data_generator.py outfile.txt
python data_generator.py outfile.txt reps=True

"""

low, high = 0, 10**6
output = sys.argv[1] if len(sys.argv) > 1 else "output.txt"

with open(output, "w") as f:
    elements = []
    for i in range(low, high):
        elements.append(random.randint(low, high))
    if len(sys.argv) == 3 and sys.argv[2].lower() != "reps=true":
        elements = set(elements)
    f.write(' '.join(str(i) for i in elements))

