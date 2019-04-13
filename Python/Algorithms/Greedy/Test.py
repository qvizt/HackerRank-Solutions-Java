from math import acos, pi

a = 2
b = 3
c = 4

maximum_perimeter = -1
try:
    alpha = acos((a * a - b * b - c * c) / (-2 * b * c)) * 180 / pi
    beta = acos((b * b - c * c - a * a) / (-2 * c * a)) * 180 / pi
    gamma = acos((c * c - a * a - b * b) / (-2 * a * b)) * 180 / pi
    max_angle = 180
    if alpha == max_angle or beta == max_angle or gamma == max_angle:
        pass
    else:
        maximum_perimeter = max(a, b, c, maximum_perimeter)
except Exception:
    pass

print(maximum_perimeter)
