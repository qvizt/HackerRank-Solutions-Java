# Solution for Closest Numbers


def get_closest_numbers(numbers):
    numbers.sort()
    result = []
    difference = 10e7 * 2  # see constraints
    for i in range(len(numbers) - 1):
        x = numbers[i]

        for k in range(i + 1, len(numbers)):
            z = numbers[k]
            d = abs(x - z)

            if d > difference:
                # quit loop because there will not be any smaller difference, because
                # the difference is growing due to the sorting of the numbers
                # at the beginning of this method
                break

            if d < difference:
                # found a smaller difference, so discard previous closest numbers
                # and update the difference
                result = []
                difference = d

            # update the result
            result.append(x)
            result.append(z)

    return result


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = get_closest_numbers(numbers)
    print(' '.join(map(str, result)))
