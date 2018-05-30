# Solution for Eye and Identity

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(sign=" ")

    n, m = map(int, input().split())

    array = numpy.eye(n, m)

    print(array)
