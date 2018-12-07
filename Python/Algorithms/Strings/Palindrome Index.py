# Solution for Palindrome Index


def get_removal_index(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            sub = s[:i] + s[i + 1:]
            if is_palindrome(sub):
                return i
            else:
                return len(s) - i - 1
    return -1


def is_palindrome(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-(i + 1)]:
            return False

    return True


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        result = get_removal_index(s)
        print(result)
