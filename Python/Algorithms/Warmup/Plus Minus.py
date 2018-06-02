# Solution for Plus Minus

# !/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0

    for val in arr:
        if val > 0:
            positive += 1
        elif val < 0:
            negative += 1
        else:
            zeroes += 1

    length = len(arr)
    print(positive / length)
    print(negative / length)
    print(zeroes / length)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
