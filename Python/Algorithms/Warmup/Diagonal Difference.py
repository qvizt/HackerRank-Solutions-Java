# Solution for Diagonal Difference

# !/bin/python3

import os


# Complete the diagonalDifference function below.
def diagonalDifference(a):
    left_to_right = 0
    right_to_left = 0

    length = len(a)
    for i in range(length):
        left_to_right += a[i][i]
        right_to_left += a[i][length - 1 - i]

    return abs(left_to_right - right_to_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
