# Solution for The Hurdle Race


if __name__ == '__main__':
    nr_hurdles, jump_height = map(int, input().split())
    max_height = max(map(int, input().split()))

    minimum_doses = max_height - jump_height
    if minimum_doses <= 1:
        minimum_doses = 0

    print(minimum_doses)
