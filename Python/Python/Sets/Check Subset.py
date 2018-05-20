# Solution for Check Subset


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        input()  # skip nr of elements in a
        a = set(map(int, input().split()))
        input()  # skip nr of elements in b
        b = set(map(int, input().split()))

        print(a.issubset(b))
