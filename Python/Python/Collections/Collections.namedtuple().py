# Solution for Collections.namedtuple()


from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    columns = input().split()

    Data = namedtuple('Data', columns)
    sum = 0
    for i in range(n):
        line = input().split()
        d = Data(*line)
        sum += int(d.MARKS)

    avg = sum / n
    print("{:.2f}".format(avg))

# less than 4 lines, but missing the point of namedtuple and PEP-8
"""
if __name__ == '__main__':
    n, columns = int(input()), input().split()
    print("{}".format(sum([int(input().split()[columns.index("MARKS")]) for i in range(n)]) / n))
"""
