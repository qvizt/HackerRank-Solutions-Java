# Solution for Manasa and Stones


def possible_numbers(a_difference, b_difference, stones):
    numbers = set()

    for a in range(0, stones):
        b = stones - 1 - a
        nr = a * a_difference + b * b_difference
        numbers.add(nr)

    numbers = list(numbers)
    numbers.sort()

    return numbers


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        non_zero_stones = int(input())  # not required?
        a_difference = int(input())
        b_difference = int(input())

        result = possible_numbers(a_difference, b_difference, non_zero_stones)
        print(*result, sep=" ")
