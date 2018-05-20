# Solution for Alphabet Rangoli


def print_rangoli(size):
    # your code goes here
    lines = [None] * (size * 2 - 1)

    width = 0

    for i in range(size):
        line = "-".join([chr(ord('a') + n - 1 - k) for k in range(i + 1)])
        line = line + line[-2:: -1]
        lines[i] = line
        lines[-i - 1] = line
        width = max(width, len(line))

    for line in lines:
        print(line.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
