# Solution for Mean, Var, and Std

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(sign=" ", legacy="1.13")  # see discussion of that challenge...
    n, m = map(int, input().split())
    a_rows = [list(map(int, input().split())) for i in range(n)]
    a = numpy.array(a_rows)

    print(numpy.mean(a, 1))
    print(numpy.var(a, 0))
    print(numpy.std(a))
