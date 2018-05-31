# Solution for Compare the Triplets

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(a, b):
    result = [0, 0]

    for i in range(len(a)):
        a_val = a[i]
        b_val = b[i]

        if a_val > b_val:
            result[0] += 1
        elif b_val > a_val:
            result[1] += 1
        else:
            continue

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
