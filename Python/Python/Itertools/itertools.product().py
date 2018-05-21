# Solution for itertools.product()


import itertools

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cart_a_b = itertools.product(a, b)

    print(*cart_a_b)
