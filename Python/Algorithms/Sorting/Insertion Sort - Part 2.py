# Solution for Insertion Sort - Part 2


def sort(numbers):
    for i in range(1, len(numbers)):
        nr = numbers[i]
        k = i - 1

        while k >= 0 and nr < numbers[k]:
            numbers[k + 1] = numbers[k]
            k -= 1

        numbers[k + 1] = nr
        print(' '.join(map(str, numbers)))


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    sort(numbers)
