# Solution for Intro to Tutorial Challenges
import bisect

if __name__ == '__main__':
    v = int(input())
    input()  # size not required
    numbers = list(map(int, input().split()))

    x = bisect.bisect_left(numbers, v, 0, len((numbers)))
    print(x)
