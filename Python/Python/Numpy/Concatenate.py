# Solution for Concatenate

import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    a = [list(map(int, input().split())) for i in range(n)]
    b = [list(map(int, input().split())) for i in range(m)]

    a = numpy.array(a)
    b = numpy.array(b)

    print(numpy.concatenate((a, b)))
