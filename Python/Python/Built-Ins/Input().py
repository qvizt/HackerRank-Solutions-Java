# Solution for Input()

if __name__ == '__main__':
    x, k = map(int, input().split())
    polynomial = input()

    result = eval(polynomial)

    print(result == k)
