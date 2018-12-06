# Solution for Separate the Numbers


def is_beautiful(s):
    length = len(s)

    for i in range(0, length // 2):  # split from n to 2 parts
        first_number_string = s[0:i + 1]
        nr = int(first_number_string)
        nr_string = str(nr)

        while len(nr_string) < length:
            nr += 1
            nr_string += str(nr)

        if nr_string == s:
            return 'YES ' + first_number_string

    return 'NO'


if __name__ == '__main__':
    nr = int(input())

    for _ in range(nr):
        s = input()
        result = is_beautiful(s)
        print(result)
