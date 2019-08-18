# Solution for Largest Permutation


def make_largest_permutation(integers, swaps):
    int_pos_map = {}
    for pos, i in enumerate(integers, 0):
        int_pos_map[i] = pos

    curr_max_int = len(integers)
    for i in range(len(integers)):
        curr_int = integers[i]
        if curr_int < curr_max_int:
            curr_max_pos = int_pos_map[curr_max_int]
            integers[i], integers[curr_max_pos] = integers[curr_max_pos], integers[i]
            int_pos_map[curr_max_int] = i
            int_pos_map[curr_int] = curr_max_pos
            swaps -= 1

        curr_max_int -= 1

        if swaps == 0:
            break


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    integers = list(list(map(int, input().split())))
    make_largest_permutation(integers, k)
    print(*integers)
