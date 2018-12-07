# Solution for Anagram


def get_minimum_number_of_changes(s):
    length = len(s)
    if length & 1:
        return -1

    half = length // 2

    # Count every char of the second half of the string
    # and save it in a dictionary.
    second_half_char_count = {}
    for c in s[half:]:
        count = second_half_char_count.get(c, 0)
        count += 1
        second_half_char_count[c] = count

    # +1 for every char in the first half of the string
    # that has no match in the second half of the string.
    nr = 0
    for c in s[:half]:
        count = second_half_char_count.get(c, 0)
        if count > 0:
            second_half_char_count[c] = count - 1
        else:
            nr += 1

    return nr


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        result = get_minimum_number_of_changes(s)
        print(result)
