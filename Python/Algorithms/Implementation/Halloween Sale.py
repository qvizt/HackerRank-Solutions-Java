# Solution for Halloween Sale


def number_of_games(price, discount, minimum_price, money):
    games = 0

    while money >= price:
        games += 1
        money -= price
        price -= discount

        if price < minimum_price:
            price = minimum_price

    return games


if __name__ == '__main__':
    price, discount, minimum_price, money = map(int, input().split())

    result = number_of_games(price, discount, minimum_price, money)
    print(result)
