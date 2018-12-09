# Solution for Correctness and the Loop Invariant


def sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):  # changed condition j > 0 to j >= 0
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    sort(numbers)
    print(' '.join(map(str, numbers)))
