# Solution for Mini-Max Sum

# !/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_value = 10 ** 9
    max_value = 0
    sum_value = 0

    for value in arr:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        sum_value += value

    sum_min = sum_value - max_value
    sum_max = sum_value - min_value
    print(sum_min, sum_max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
