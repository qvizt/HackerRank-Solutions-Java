# Solution for Day 29 Bitwise AND

# Taken from the editorial; the approach described in the example is too slow
# in Python and the test cases fail due time restriction.

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        a = k - 1
        b = ~a & -~a
        if a | b > n:
            print(a - 1)
        else:
            print(a)
