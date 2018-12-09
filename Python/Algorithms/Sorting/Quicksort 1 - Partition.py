# Solution for Quicksort 1 - Partition


def partition(numbers):
    pivot = numbers[0]

    left = 1
    right = len(numbers) - 1
    while True:
        while numbers[left] < pivot and left < len(numbers) - 1:
            left += 1

        while numbers[right] >= pivot and right > 0:
            right -= 1

        if left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        else:
            break

    if numbers[right] < pivot:
        numbers[right], numbers[0] = numbers[0], numbers[right]


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = partition(numbers)
    print(' '.join(map(str, numbers)))
