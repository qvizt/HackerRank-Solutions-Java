# Solution for DefaultDict Tutorial
"""
What to learn:

The default dictionary inserts for each non-existing
key a new value of the type that has been passed on
initialization of the default dictionary.
"""

from collections import defaultdict


if __name__ == '__main__':
    d = defaultdict(list)

    n, m = map(int, input().split())

    for i in range(n):
        char = input()
        d[char].append((i + 1))  # store the index of the char in the list

    for i in range(m):
        char = input()
        index_list = d[char]
        if index_list:
            print(*index_list)
        else:
            print(-1)
