# Solution for Taum and Bday


def minimum_cost(black_gifts, white_gifts, black_cost, white_cost, convert_cost):
    cost = 0

    if (black_cost + convert_cost) < white_cost:
        cost = black_cost * black_gifts
        cost += black_cost * white_gifts + convert_cost * white_gifts
    elif (white_cost + convert_cost) < black_cost:
        cost = white_cost * white_gifts
        cost += white_cost * black_gifts + convert_cost * black_gifts
    else:
        cost = black_cost * black_gifts + white_cost * white_gifts

    return cost


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        black_gifts, white_gifts = map(int, input().split())
        black_cost, white_cost, convert_cost = map(int, input().split())

        result = minimum_cost(black_gifts, white_gifts, black_cost, white_cost, convert_cost)
        print(result)
