# Solution for Linear Algebra

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(legacy="1.13")  # see discussion of that challenge...

    n = int(input())
    a_rows = [list(map(float, input().split())) for i in range(n)]

    print(numpy.linalg.det(a_rows))