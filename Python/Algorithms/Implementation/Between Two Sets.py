# Solution for Between Two Sets


def get_total_x(a, b):
    l = a[0]
    for i in range(1, len(a)):
        l = lcm(l, a[i])

    g = b[0]
    for i in range(1, len(b)):
        g = gcd(g, b[i])

    x = 0
    l_multiple = l
    while l_multiple <= g:
        if g % l_multiple == 0:
            x += 1
        l_multiple += l

    return x


def lcm(x, y):
    return (y / gcd(x, y)) * x


def gcd(x, y):
    while y > 0:
        x, y = y, x % y

    return x


if __name__ == '__main__':
    input()  # n and m not required
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = get_total_x(a, b)

    print(result)
