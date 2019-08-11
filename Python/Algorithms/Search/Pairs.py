# Solution for Pairs


def get_number_of_pairs(numbers, k):
    number_of_pairs = 0
    numbers.sort()

    current_index = 0
    next_index = 1
    limit = len(numbers) - 1

    while current_index < limit:
        current_nr = numbers[current_index]
        next_nr = numbers[next_index]
        difference = next_nr - current_nr

        while difference < k and next_index < limit:
            next_index += 1
            next_nr = numbers[next_index]
            difference = next_nr - current_nr

        if difference == k:
            number_of_pairs += 1

        current_index += 1

    return number_of_pairs


if __name__ == '__main__':
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = get_number_of_pairs(numbers, k)
    print(result)
