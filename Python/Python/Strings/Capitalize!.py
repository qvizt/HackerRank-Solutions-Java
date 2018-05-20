# Solution for Capitalize!

def capitalize(string):
    # not going for the easy way on purpose
    splitted = string.split(" ")
    for i in range(len(splitted)):
        s = splitted[i]
        if len(s):
            ord_first = ord(s[0])
            if 97 <= ord_first <= 122: # see ascii table
                splitted[i] = chr(ord_first - 32) + s[1:]
    return " ".join(splitted)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
