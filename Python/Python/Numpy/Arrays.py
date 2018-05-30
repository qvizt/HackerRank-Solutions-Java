# Solution for Arrays

import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    array = numpy.array(arr, float)
    array = array[::-1]  # Alternative: numpy.flipud(array)
    return array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
