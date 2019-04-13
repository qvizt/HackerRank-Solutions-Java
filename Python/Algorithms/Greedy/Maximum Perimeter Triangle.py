# Solution for Maximum Perimeter Triangle
#
# Useful sources:
# [1] https://de.wikipedia.org/wiki/Dreieck#SSS-Fall
# [2] https://de.wikipedia.org/wiki/Radiant_(Einheit)
# [3] https://en.wikipedia.org/wiki/Degeneracy_(mathematics)#Triangle

from math import acos, pi


def get_maximum_perimeter_triangle(sticks):
    sticks.sort()
    maximum_triangle = (-1, -1, -1)

    for i in range(len(sticks) - 2):
        a = sticks[i]
        b = sticks[i + 1]
        c = sticks[i + 2]

        try:
            alpha = acos((a * a - b * b - c * c) / (-2 * b * c)) * 180 / pi
            beta = acos((b * b - c * c - a * a) / (-2 * c * a)) * 180 / pi
            gamma = acos((c * c - a * a - b * b) / (-2 * a * b)) * 180 / pi
            angle = 180
            if alpha == angle or beta == angle or gamma == angle:
                # skip 180 degree angle solutions (= degenerated triangle)
                pass
            else:
                current_triangle = (c, b, a)
                if current_triangle > maximum_triangle:
                    maximum_triangle = current_triangle
        except Exception:
            # skip solutions with undefined angles
            pass

    if maximum_triangle[0] == -1:
        return -1
    else:
        return '{} {} {}'.format(maximum_triangle[2], maximum_triangle[1], maximum_triangle[0])


if __name__ == '__main__':
    input()  # skip n
    sticks = list(map(int, input().split()))
    perimeter = get_maximum_perimeter_triangle(sticks)
    print(perimeter)
