# Solution for Maximize It!


import itertools

if __name__ == '__main__':
    k, m = map(int, input().split())

    lists = []
    for i in range(k):
        # slice start at 1 because index 0 contains the length of the list
        li = map(int, input().split()[1:])

        # store the squares in the list
        li = list(map(lambda x: x ** 2, li))

        lists.append(li)

    # generate all possible pairings
    products = itertools.product(*lists)

    # sum the squares of each pairing and apply modulo
    sums = list(map(lambda x: sum(x) % m, products))

    print(max(sums))
