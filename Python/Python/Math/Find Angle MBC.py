# Solution for Find Angle MBC

import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    result = AB / BC
    result = math.degrees(math.atan(result))

    print(str(round(result)) + "°")

"""
Important (21.05.2018):
It seems to be that the angles in the solution are for
MCB and not MBC (needs to be verified).

The correct solution seems to be to calculate
the tangent via AB / BC to get the angle in C and
then subtract this angle from angle M (90).

"""
