# Solution for Day 25 Running Time and Complexity

from math import sqrt


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True


n = int(input())

for i in range(n):
    nr = int(input())
    if isPrime(nr):
        print("Prime")
    else:
        print("Not prime")
