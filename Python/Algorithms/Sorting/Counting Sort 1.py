# Solution for Counting Sort 1


def get_array(numbers):
    li = [0] * 100

    for n in numbers:
        li[n] += 1

    return li


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = get_array(numbers)
    print(' '.join(map(str, result)))
