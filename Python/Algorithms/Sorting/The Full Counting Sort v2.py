# Solution for The Full Counting Sort
#
# Be aware that this way of solving the
# challenge is kinda cheating :)
# I use Python's sort and the way how
# tuples are handled in that sort method.

if __name__ == '__main__':
    n = int(input())
    items = []

    half = n // 2
    i = 0
    while i < half:
        nr, s = input().split()
        items.append((int(nr), i, '-'))
        i += 1

    while i < n:
        nr, s = input().split()
        items.append((int(nr), i, s))
        i += 1

    items.sort()
    print(' '.join(x[2] for x in items))
