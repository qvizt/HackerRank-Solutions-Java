# Solution for Array Mathematics

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a_rows = [list(map(int, input().split())) for i in range(n)]
    b_rows = [list(map(int, input().split())) for i in range(n)]

    a = numpy.array(a_rows, int)
    b = numpy.array(b_rows, int)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)
