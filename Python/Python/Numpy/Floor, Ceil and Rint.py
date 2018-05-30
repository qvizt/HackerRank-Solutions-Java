# Solution for Floor, Ceil and Rint

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(sign=" ")

    a_data = list(map(float, input().split()))
    a = numpy.array(a_data)

    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))
