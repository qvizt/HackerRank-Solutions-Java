# Solution for Dot and Cross

import numpy

if __name__ == '__main__':
    n = int(input())

    a_rows = [list(map(int, input().split())) for i in range(n)]
    b_rows = [list(map(int, input().split())) for i in range(n)]

    a = numpy.array(a_rows)
    b = numpy.array(b_rows)

    print(numpy.dot(a, b))
