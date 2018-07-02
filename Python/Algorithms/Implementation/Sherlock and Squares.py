# Solution for Sherlock and Squares
import math


def count_squares(lower_bound, upper_bound):
    count = 0
    lower_bound = math.ceil(math.sqrt(lower_bound))
    upper_bound = int(math.sqrt(upper_bound))

    count += upper_bound - int(lower_bound) + 1

    return count


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        lower_bound, upper_bound = map(int, input().split())
        result = count_squares(lower_bound, upper_bound)
        print(result)
