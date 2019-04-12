# Solution for Minimum Absolute Difference in an Array


def get_mininum_absolute_difference(numbers):
    numbers.sort()
    difference = abs(numbers[0] - numbers[len(numbers) - 1])
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < difference:
            difference = diff

    return difference


if __name__ == '__main__':
    input()  # skip n
    numbers = list(map(int, input().split()))
    difference = get_mininum_absolute_difference(numbers)
    print(difference)
