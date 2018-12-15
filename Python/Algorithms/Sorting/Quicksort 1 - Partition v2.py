# Solution for Quicksort 1 - Partition
# This version uses three lists to
# partition the numbers.


def partition(numbers):
    left = []
    equal = []
    right = []

    equal.append(numbers[0])

    for i in range(1, len(numbers)):
        if numbers[i] < equal[0]:
            left.append(numbers[i])
        elif numbers[i] > equal[0]:
            right.append(numbers[i])
        else:
            equal.append(numbers[i])

    return left + equal + right


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = partition(numbers)
    print(' '.join(map(str, result)))
