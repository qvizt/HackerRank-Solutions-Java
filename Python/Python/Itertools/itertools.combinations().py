# Solution for itertools.combinations()

import itertools

if __name__ == '__main__':
    split_input = input().split()
    s = sorted(split_input[0])
    k = int(split_input[1])

    for i in range(k):
        for comb in itertools.combinations(s, i + 1):
            print("".join(comb))
