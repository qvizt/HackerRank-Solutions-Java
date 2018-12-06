# Solution for Alternating Characters


def get_number_of_deletions(s):
    nr = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            nr += 1

    return nr


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        result = get_number_of_deletions(s)
        print(result)
