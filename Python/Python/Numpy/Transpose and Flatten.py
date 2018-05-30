# Solution for Transpose and Flatten

import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    rows = [list(map(int, input().split())) for i in range(n)]
    array = numpy.array(rows)

    print(array.transpose())
    print(array.flatten())
