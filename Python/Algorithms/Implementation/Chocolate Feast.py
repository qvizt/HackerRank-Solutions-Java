# Solution for Chocolate Feast


def number_of_chocolates(money, cost, required_wrappers):
    chocolates = money // cost
    wrappers = chocolates

    while wrappers >= required_wrappers:
        wrappers = wrappers - required_wrappers
        chocolates += 1
        wrappers += 1

    return chocolates


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        money, cost, required_wrappers = map(int, input().split())

        result = number_of_chocolates(money, cost, required_wrappers)
        print(result)
