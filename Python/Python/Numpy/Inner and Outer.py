# Solution for Inner and Outer

import numpy

if __name__ == '__main__':
    a_row = list(map(int, input().split()))
    b_row = list(map(int, input().split()))

    a = numpy.array(a_row)
    b = numpy.array(b_row)

    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
