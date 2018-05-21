# Solution for itertools.permutations()

import itertools

if __name__ == '__main__':
    split_input = input().split()
    s = sorted(split_input[0])
    k = int(split_input[1])

    for perm in itertools.permutations(s, k):
        print("".join(perm))
