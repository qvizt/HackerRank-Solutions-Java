# Solution for Fair Rations


def loaves_distribution(loaves):
    count = 0

    for i in range(len(loaves) - 1):
        if loaves[i] & 1:
            loaves[i] += 1
            loaves[i + 1] += 1
            count += 2

    return count if loaves[len(loaves) - 1] & 1 == 0 else "NO"


if __name__ == '__main__':
    input()  # number of people not relevant
    loaves = list(map(int, input().split()))

    result = loaves_distribution(loaves)
    print(result)
