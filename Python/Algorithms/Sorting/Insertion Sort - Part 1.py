# Solution for Insertion Sort - Part 1


def _print(numbers):
    print(' '.join(map(str, numbers)))


if __name__ == '__main__':
    index = int(input()) - 1  # using the size as index
    numbers = list(map(int, input().split()))

    nr = numbers[index]
    while index > 0 and nr < numbers[index - 1]:
        numbers[index] = numbers[index - 1]
        index -= 1
        _print(numbers)
    else:
        numbers[index] = nr

    _print(numbers)
