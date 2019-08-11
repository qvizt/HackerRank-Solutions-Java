# Solution for Beautiful Pairs


def get_beautiful_pair_count(a, b):
    left_indices = set()
    right_indices = set()
    b_pos = {}
    pair_count = 0

    for i, v in enumerate(b):
        pos = b_pos.get(v, set())
        pos.add(i)
        b_pos[v] = pos

    for i, v in enumerate(a):
        pos = b_pos.get(v, None)
        if pos is not None:
            p_count = 0
            for p in pos:
                if p not in right_indices:
                    right_indices.add(p)
                    pair_count += 1
                    p_count += 1
                    break
            if p_count == len(pos):
                b_pos.pop(v)
        else:
            left_indices.add(i)

    if len(left_indices) > 0:
        pair_count += 1
    else:
        # If it was possible to make a pair for every element in a
        # without any duplicate indices we have to subtract -1
        # because the note in the problem states that an element
        # of b has to be changed before the creation of the pairs.
        pair_count -= 1

    return pair_count


if __name__ == '__main__':
    input()  # skip n
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = get_beautiful_pair_count(a, b)
    print(result)
