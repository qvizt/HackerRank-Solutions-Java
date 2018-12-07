# Solution for String Construction


def get_minimum_constructing_cost(s):
    cost = 0
    p = set()

    for c in s:
        if c not in p:
            cost += 1
            p.add(c)

    return cost


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        result = get_minimum_constructing_cost(s)
        print(result)
