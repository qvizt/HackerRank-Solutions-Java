# Solution for Strange Counter


def value(time):
    tm = 1

    # Pattern for time at the beginning of a cycle (for cycle nr > 1)
    # is PREVIOUS CYCLE START TIME * 2 + 2
    while True:
        tm = tm * 2 + 2

        if tm > time:
            tm = (tm - 2) // 2
            break

    # value decreased by 1 for an increase in time by 1, so the difference
    # between time and cycle start time can be used to compute the value for
    # a specific time.
    #
    # NOTE: the start value of a cycle is time + 2
    vl = tm + 2 - (time - tm)

    return vl


if __name__ == '__main__':
    time = int(input())

    result = value(time)
    print(result)
