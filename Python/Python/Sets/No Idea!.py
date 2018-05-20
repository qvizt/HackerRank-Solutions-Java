# Solution for No Idea!

if __name__ == '__main__':
    input()  # skip first input
    elements = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    happiness = 0

    for value in elements:
        if value in a:
            happiness += 1
        elif value in b:
            happiness -= 1

    print(happiness)
