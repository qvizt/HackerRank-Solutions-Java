# Solution for Luck Balance


def get_maximum_luck(contests, loss_count):
    luck_values = []
    maximum_luck = 0

    for c in contests:
        luck = c[0]
        rating = c[1]

        if rating == 1:
            luck_values.append(luck)
        else:
            maximum_luck += luck

    luck_values.sort()
    limit = max(len(luck_values) - loss_count, 0)

    for i in range(0, limit):
        maximum_luck -= luck_values[i]

    for i in range(limit, len(luck_values)):
        maximum_luck += luck_values[i]

    return maximum_luck


if __name__ == '__main__':
    contest_count, loss_count = list(map(int, input().split()))
    contests = []
    for _ in range(contest_count):
        contest_data = list(map(int, input().split()))
        contests.append(contest_data)

    max_luck = get_maximum_luck(contests, loss_count)
    print(max_luck)
