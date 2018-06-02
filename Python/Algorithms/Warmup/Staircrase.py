# Solution for Staircrase

# !/bin/python3

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print("{:>{}}".format("#" * (i + 1), n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
