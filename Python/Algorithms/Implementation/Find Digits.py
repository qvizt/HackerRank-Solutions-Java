# Solution for Find Digits


def count_divisors(nr_string):
    count = 0
    nr = int(nr_string)

    for c in nr_string:
        d = int(c)

        if d and not nr % d:
            count += 1

    return count


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        nr_string = input()

        result = count_divisors(nr_string)
        print(result)
