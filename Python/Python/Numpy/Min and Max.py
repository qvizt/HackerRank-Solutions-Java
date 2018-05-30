# Solution for Min and Max

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a_rows = [list(map(int, input().split())) for i in range(n)]
    a = numpy.array(a_rows)

    min_a = numpy.min(a, 1)
    max_min_a = numpy.max(min_a)

    print(max_min_a)
