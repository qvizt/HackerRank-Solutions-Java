# Solution for Iterables and Iterators


import itertools

if __name__ == '__main__':
    input()  # not required
    letters = input().split()
    k = int(input())
    combinations = list(itertools.combinations(letters, k))

    a_count = 0

    for comb in combinations:
        if 'a' in comb:
            a_count += 1

    probability = a_count / len(combinations)
    print("{:.3f}".format(probability))
