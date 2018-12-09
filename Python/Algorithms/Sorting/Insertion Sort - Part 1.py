# Solution for Insertion Sort - Part 1


def sort_last_number(numbers):
    index = len(numbers) - 1
    nr = numbers[index]

    while index > 0 and nr < numbers[index - 1]:
        numbers[index] = numbers[index - 1]
        index -= 1
        _print(numbers)

    numbers[index] = nr
    _print(numbers)


def _print(numbers):
    print(' '.join(map(str, numbers)))


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    sort_last_number(numbers)
