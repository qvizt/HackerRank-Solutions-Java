# Solution for Non-Divisible Subset
from collections import defaultdict


def size_largest_subset(values, factor):
    remainder_counters = defaultdict(int)

    for v in values:
        remainder = v % factor
        remainder_counters[remainder] += 1

    count = 0
    for i in range(factor // 2 + 1):
        if factor == i * 2 or i == 0:
            count += min(remainder_counters[i], 1)
        else:
            count += max(remainder_counters[i], remainder_counters[factor - i])

    return count


if __name__ == '__main__':
    n, factor = map(int, input().split())  # n not required
    values = set(map(int, input().split()))

    result = size_largest_subset(values, factor)
    print(result)
