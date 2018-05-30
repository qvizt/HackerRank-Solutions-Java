# Solution for Sum and Prod

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a_rows = [list(map(int, input().split())) for i in range(n)]
    a = numpy.array(a_rows)

    sum_a = numpy.sum(a, 0)
    product_a = numpy.product(sum_a)

    print(product_a)
