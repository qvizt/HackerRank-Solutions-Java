# Solution for Viral Advertising


def nr_cumulative_likes(days):
    liked = 5 // 2
    cumulative = liked

    for _ in range(2, days + 1):
        liked = (liked * 3) // 2
        cumulative += liked

    return cumulative


if __name__ == '__main__':
    days = int(input())

    result = nr_cumulative_likes(days)
    print(result)
