# Solution for Set .union() Operation

if __name__ == '__main__':
    n = int(input())
    n_numbers = set(map(int, input().split(" ")))
    b = int(input())
    b_numbers = set(map(int, input().split(" ")))

    print(len(n_numbers.union(b_numbers)))
