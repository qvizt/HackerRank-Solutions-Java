# Solution for Utopian Tree


def height(cycles):
    h = 1

    for c in range(1, cycles + 1):
        if c & 1:
            h *= 2
        else:
            h += 1

    return h


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        cycles = int(input())
        result = height(cycles)
        print(result)
