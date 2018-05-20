# Solution for Set .difference() Operation


if __name__ == '__main__':
    n = int(input())
    n_numbers = set(map(int, input().split(" ")))
    b = int(input())
    b_numbers = set(map(int, input().split(" ")))

    print(len(n_numbers.difference(b_numbers)))
