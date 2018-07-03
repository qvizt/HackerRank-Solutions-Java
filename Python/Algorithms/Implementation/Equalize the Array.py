# Solution for Equalize the Array


def min_deletions_to_equalize(numbers):
    di = {}
    for n in numbers:
        count = di.get(n, 0)
        count += 1
        di[n] = count

    max_occurrences = max(di.values())
    deletions_count = len(numbers) - max_occurrences

    return deletions_count


if __name__ == '__main__':
    input()  # n not required
    numbers = list(map(int, input().split()))

    result = min_deletions_to_equalize(numbers)
    print(result)
