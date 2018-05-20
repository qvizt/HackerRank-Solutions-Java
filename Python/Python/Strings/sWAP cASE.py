# Solution for sWAP cASE

def swap_case(s):
    # Easy way
    # return s.swapcase()

    # Solution via ascii table
    chars = []

    for c in s:
        ord_c = ord(c)
        if 65 <= ord_c <= 90:
            ord_c = ord_c + 32
        elif 97 <= ord_c <= 122:
            ord_c = ord_c - 32

        chars.append(chr(ord_c))

    return "".join(chars)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
