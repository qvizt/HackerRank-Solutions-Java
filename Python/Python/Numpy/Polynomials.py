# Solution for Polynomials

import numpy

if __name__ == '__main__':
    p = list(map(float, input().split()))
    x = float(input())

    print(numpy.polyval(p, x))