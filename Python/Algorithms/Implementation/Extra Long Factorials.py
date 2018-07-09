# Solution for Extra Long Factorials

def factorial(n):
    fac = 1

    for i in range(2, n + 1):
        fac *= i

    return fac


if __name__ == '__main__':
    n = int(input())

    result = factorial(n)
    print(result)
