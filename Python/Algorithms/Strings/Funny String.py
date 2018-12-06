# Solution for Funny String


def is_funny(s):
    rev = s[::-1]

    s_differences = get_differences(s)
    rev_differences = get_differences(rev)

    return s_differences == rev_differences


def get_differences(s):
    differences = []

    for i in range(len(s) - 1):
        first = ord(s[i])
        second = ord(s[i + 1])
        diff = abs(first - second)
        differences.append(diff)

    return differences


if __name__ == '__main__':
    nr = int(input())

    for _ in range(nr):
        s = input()
        result = 'Funny' if is_funny(s) else 'Not Funny'
        print(result)
