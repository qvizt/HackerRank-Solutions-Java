# Solution for Making Anagrams


def get_minimum_deletions(s, t):
    nr = 0
    for c in s:
        if c in t:
            t = t.replace(c, '', 1)
            nr += 1

    return len(s) + len(t) - nr


if __name__ == '__main__':
    s = input()
    t = input()

    result = get_minimum_deletions(s, t)
    print(result)
