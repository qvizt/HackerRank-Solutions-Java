# Solution for Game of Thrones - I


def can_be_a_palindrome(s):
    char_count = {}
    for c in s:
        count = char_count.get(c, 0)
        char_count[c] = count + 1

    odd_existing = False
    for v in char_count.values():
        if v & 1:
            if odd_existing:
                return 'NO'
            else:
                odd_existing = True

    return 'YES'


if __name__ == '__main__':
    s = input()
    result = can_be_a_palindrome(s)
    print(result)
