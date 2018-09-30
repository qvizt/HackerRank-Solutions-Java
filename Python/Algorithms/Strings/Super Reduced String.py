# Solution for Super Reduced String


def reduce_string(string):
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            if i + 2 < len(string):
                string = string[0:i] + string[i + 2:]
            else:
                string = string[0:i]
            i = 0
        else:
            i += 1

    return string if len(string) > 0 else "Empty String"


if __name__ == '__main__':
    s = input()

    s = reduce_string(s)

    print(s)
