# Solution for Beautiful Days at the Movies


def beautiful_days(start, end, k):
    counter = 0

    for day in range(start, end + 1):
        reverse_day = str(day)[::-1]
        reverse_day = int(reverse_day)
        difference = abs(day - reverse_day)
        if difference % k == 0:
            counter += 1

    return counter


if __name__ == '__main__':
    start, end, k = map(int, input().split())

    result = beautiful_days(start, end, k)
    print(result)
