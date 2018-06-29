# Solution for Kangaroo


def meet(x1, v1, x2, v2):
    if x1 > x2:
        distance = x1 - x2
        progress = v2 - v1
    else:
        distance = x2 - x1
        progress = v1 - v2

    if progress > 0 and distance % progress == 0:
        return "YES"

    return "NO"


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())

    result = meet(x1, v1, x2, v2)

    print(result)
