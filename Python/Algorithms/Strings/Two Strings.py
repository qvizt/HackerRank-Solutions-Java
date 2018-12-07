# Solution for Two Strings


def has_common_substring(s, t):
    for c in s:
        if c in t:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        t = input()
        result = has_common_substring(s, t)
        print(result)
