# Solution for Check Strict Superset


if __name__ == '__main__':
    a = set(map(int, input().split()))

    n = int(input())

    is_strict = True

    for i in range(n):
        b = set(map(int, input().split()))
        if not a > b:
            is_strict = False

    print(is_strict)
