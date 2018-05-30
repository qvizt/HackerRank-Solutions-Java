# Solution for Shape and Reshape

import numpy

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    array = numpy.array(numbers)
    print(numpy.reshape(array, (3, 3)))
