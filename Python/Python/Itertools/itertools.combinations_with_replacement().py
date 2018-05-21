# Solution for itertools.combinations_with_replacement()


import itertools

if __name__ == '__main__':
    split_input = input().split()
    s = sorted(split_input[0])
    k = int(split_input[1])

    for comb in itertools.combinations_with_replacement(s, k):
        print("".join(comb))
