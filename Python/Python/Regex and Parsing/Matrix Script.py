# Solution for Matrix Script

# !/bin/python3

import math
import os
import random
import re
import sys

nm = input().split()
n = int(nm[0])
m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

zipped = zip(*matrix)

s = ""
for z in zipped:
    s += "".join(z)

result = re.sub(r"\b\W+\b", " ", s)
print(result)
