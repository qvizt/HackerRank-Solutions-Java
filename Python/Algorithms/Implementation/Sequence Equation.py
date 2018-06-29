# Solution for Sequence Equation


def y(x, sequence):
    for i in range(len(sequence)):
        if x == sequence[i]:
            i = i + 1  # +1 due 0-based index
            for k in range(len(sequence)):
                if i == sequence[k]:
                    return k + 1  # +1 due 0-based index


if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))

    for i in range(1, n + 1):
        result = y(i, sequence)
        print(result)
