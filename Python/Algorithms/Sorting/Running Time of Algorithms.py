# Solution for Running Time of Algorithms


def sort(numbers):
    shifts = 0
    for i in range(1, len(numbers)):
        nr = numbers[i]
        k = i - 1

        while k >= 0 and nr < numbers[k]:
            numbers[k + 1] = numbers[k]
            k -= 1
            shifts += 1

        numbers[k + 1] = nr

    print(shifts)


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    sort(numbers)
