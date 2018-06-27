# Solution for Divisible Sum Pairs


def count_divisible_sum_pairs(array, k):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if not (array[i] + array[j]) % k:
                count += 1
    return count


if __name__ == '__main__':
    n, k = map(int, input().split())  # = array length, k = divisor
    array = list(map(int, input().split()))

    count = count_divisible_sum_pairs(array, k)
    print(count)
