# Solution for Day 7 Arrays

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
rev = map(str, reversed(arr))
rev_string = " ".join(rev)
print(rev_string)