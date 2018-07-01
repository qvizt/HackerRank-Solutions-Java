# Solution for Append and Delete


def transformation_possible(s, t, nr_ops):
    is_possible = "No"
    prefix_length = 0

    short_string, long_string = (s, t) if len(s) < len(t) else (t, s)

    for i in range(len(short_string)):
        if short_string[i] == long_string[i]:
            prefix_length += 1
        else:
            break

    required_ops_without_prefix = len(s) + len(t) - 2 * prefix_length
    remaining_ops = nr_ops - required_ops_without_prefix

    if remaining_ops == 0:  # It is possible to consume all operations
        is_possible = "Yes"
    elif remaining_ops > 0:
        if remaining_ops % 2 == 0:  # delete and append to consume operations
            is_possible = "Yes"
        elif nr_ops >= (len(s) + len(t)):
            # deleting all chars from s is possible and appending chars
            # for t is possible too
            is_possible = "Yes"

    return is_possible


if __name__ == '__main__':
    s = input()
    t = input()
    nr_ops = int(input())

    result = transformation_possible(s, t, nr_ops)
    print(result)
