# Solution for Zeros and Ones

import numpy

if __name__ == '__main__':
    dimensions = tuple(map(int, input().split()))
    zeroes = numpy.zeros(dimensions, int)
    ones = numpy.ones(dimensions, int)

    print(zeroes)
    print(ones)