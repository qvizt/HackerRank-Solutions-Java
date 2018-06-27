# Solution for Counting Valleys


def number_of_valleys(s):
    level = 0
    in_valley = False
    valleys = 0

    for step in s:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1

        if level < 0 and not in_valley:
            in_valley = True
        elif level == 0 and in_valley:
            in_valley = False
            valleys += 1

    return valleys


if __name__ == '__main__':
    input()  # n not required
    s = input()  # the path

    valleys = number_of_valleys(s)
    print(valleys)
