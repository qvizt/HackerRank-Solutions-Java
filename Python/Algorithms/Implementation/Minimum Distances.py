# Solution for Minimum Distances


def minimum_distance(numbers):
    distance = len(numbers)

    for i in range(len(numbers)):
        k_excl_index = i + distance

        if k_excl_index > len(numbers):
            k_excl_index = len(numbers)

        for k in range(i + 1, k_excl_index):
            if numbers[i] == numbers[k] and k - i < distance:
                distance = k - i
                break

        if distance == 1:
            break

    if distance == len(numbers):
        distance = -1

    return distance


if __name__ == '__main__':
    input()  # n is not required
    numbers = list(map(int, input().split()))

    result = minimum_distance(numbers)
    print(result)
