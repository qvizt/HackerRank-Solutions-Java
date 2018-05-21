# Solution for Polar Coordinates


import cmath

if __name__ == '__main__':
    z = complex(input())
    r = abs(z)
    phi = cmath.phase(z)

    print("{:.3f}".format(r))
    print("{:.3f}".format(phi))
