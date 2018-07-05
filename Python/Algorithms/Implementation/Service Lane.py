# Solution for Service Lane


def maximum_vehicle_size(start, end, widths):
    size = min(widths[start:end + 1])

    return size


if __name__ == '__main__':
    measurements, test_cases = map(int, input().split())
    widths = list(map(int, input().split()))

    for _ in range(test_cases):
        start, end = map(int, input().split())

        result = maximum_vehicle_size(start, end, widths)
        print(result)
