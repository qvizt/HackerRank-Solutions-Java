# Solution for The Full Counting Sort


if __name__ == '__main__':
    n = int(input())
    d = {}
    half = n // 2
    i = 0

    while i < half:
        nr, s = input().split()
        li = d.get(nr, [])
        li.append('-')
        d[nr] = li
        i += 1

    while i < n:
        nr, s = input().split()
        li = d.get(nr, [])
        li.append(s)
        d[nr] = li
        i += 1

    keys = sorted(d.keys(), key=int)
    for k in keys:
        print(' '.join(d[k]), end=' ')
