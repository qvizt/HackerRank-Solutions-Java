# Solution for Find the Median


def get_median(numbers):
    numbers.sort()
    length = len(numbers)
    index = length // 2  # calculation based on the assumption that length is an odd number

    if not length & 1:  # length is an even number, so subtract 1
        index -= 1

    return numbers[index]


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = get_median(numbers)
    print(result)
