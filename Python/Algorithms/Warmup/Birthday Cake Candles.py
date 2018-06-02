# Solution for Birthday Cake Candles

# !/bin/python3

import os


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_height = 1
    count = 0
    for value in ar:
        if value > max_height:
            max_height = value
            count = 1
        elif value == max_height:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
