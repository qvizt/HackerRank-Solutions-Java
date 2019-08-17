# Solution for Sherlock and The Beast


def get_decent_number(n):
    threes, r = divmod(n, 3)
    fives = 0

    if threes > 0:
        if r == 2:
            fives += 1
            threes -= 1
            r = 0
        elif r == 1 and threes > 2:  # nr of 3s greater 2 for skipping wrong result for 7
            fives += 2
            threes -= 2
            r = 0

    s = '-1'

    if r == 0:
        s = ''
        while fives > 0:
            s += '33333'
            n -= 5
            fives -= 1

        while n > 0:
            s = '555' + s
            n -= 3

    return s


if __name__ == '__main__':
    nr_tests = int(input())

    for _ in range(nr_tests):
        n = int(input())
        decent_nr = get_decent_number(n)
        print(decent_nr)
