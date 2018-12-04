# Solution for Weighted Uniform Strings


def get_set_of_weights(uniform_string):
    set_weights = set()
    prev_read_char = None
    sum = 0

    for i in range(0, len(uniform_string)):
        c = uniform_string[i]
        weight = ord(c) - 96
        if c == prev_read_char:
            sum = sum + weight
        else:
            sum = weight
        prev_read_char = c
        set_weights.add(sum)

    return set_weights


if __name__ == '__main__':
    s = input()
    weights = get_set_of_weights(s)

    n = int(input())

    for _ in range(n):
        i = int(input())

        print('Yes' if i in weights else 'No')
