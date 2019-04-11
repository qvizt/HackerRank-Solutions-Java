# Solution for Sherlock and Array


def is_balanced_sum_possible(numbers):
    if len(numbers) == 1:
        return 'YES'

    left_sum = 0
    right_sum = 0

    # First iteration: different approach than the following iterations
    for i in range(1, len(numbers)):
        right_sum += numbers[i]

    if left_sum == right_sum:
        return 'YES'

    # Following iterations: Simply add a number to left_sum and
    # subtract a number of right_sum
    index = 1
    while index < len(numbers):
        left_sum += numbers[index - 1]
        right_sum -= numbers[index]
        if left_sum == right_sum:
            return 'YES'
        index += 1

    return 'NO'


if __name__ == '__main__':
    tests = int(input())
    for _ in range(tests):
        input()  # skip n
        numbers = [int(x) for x in input().split()]
        result = is_balanced_sum_possible(numbers)
        print(result)
