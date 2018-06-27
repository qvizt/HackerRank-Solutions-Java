# Solution for Drawing Book
import math


def page_turns(n, p):
    half = n // 2
    if p <= half:
        turns = p // 2
    else:
        if n & 1:
            turns = (n - p) // 2
        else:
            turns = (n - p + 1) // 2

    return turns


if __name__ == '__main__':
    n = int(input())
    p = int(input())

    turns = page_turns(n, p)
    print(turns)
