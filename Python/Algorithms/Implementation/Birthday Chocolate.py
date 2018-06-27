# Solution for Birthday Chocolate


def count_segments(s, d, m):
    nr_segments = 0
    for i in range(len(s) - m + 1):
        sum_d = sum(s[i:i + m])

        if sum_d == d:
            nr_segments += 1

    return nr_segments


if __name__ == '__main__':
    input()  # skip n
    s = list(map(int, input().split()))
    d, m = map(int, input().split())  # d = sum, m = length

    result = number_of_segments(s, d, m)
    print(result)
