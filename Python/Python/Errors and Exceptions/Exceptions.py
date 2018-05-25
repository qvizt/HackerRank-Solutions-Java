# Solution for Exceptions

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except (ValueError, ZeroDivisionError) as ex:

            print("Error Code:", ex)
