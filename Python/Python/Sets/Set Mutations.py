# Solution for Set Mutations


if __name__ == '__main__':
    n = int(input())

    a = set(map(int, input().split()))

    n = int(input()) * 2

    while n:
        splitted_line = input().split()
        operation = splitted_line[0]

        b = set(map(int, input().split()))

        if operation == "intersection_update":
            a &= b
        elif operation == "update":
            a |= b
        elif operation == "symmetric_difference_update":
            a ^= b
        else:
            a -= b

        n -= 2 # -2 because 2 inputs

    print(sum(a))
