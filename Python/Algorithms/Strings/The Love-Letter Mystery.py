# Solution for The Love-Letter Mystery


def get_minimum_operations_for_palindrome(s):
    operations = 0
    limit = len(s) // 2

    for i in range(limit):
        # assume that one value is greater than another
        greater = ord(s[i])
        less = ord(s[-(i + 1)])

        # assumption was wrong? Fix it
        if greater < less:
            greater, less = less, greater

        while greater > less:
            greater -= 1
            operations += 1

    return operations


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        result = get_minimum_operations_for_palindrome(s)
        print(result)
