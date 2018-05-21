# Solution for Compress the String!

import itertools

if __name__ == '__main__':
    s = input()

    for k, g in itertools.groupby(s):
        Xc = (len(list(g)), int(k))
        print(Xc, end=" ")