# Solution for Day 10 Binary Numbers

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    max_consecutive = 0
    consecutive = 0

    while n > 0:
        if n % 2 == 1:
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 0
        n = n // 2

    print(max_consecutive)
