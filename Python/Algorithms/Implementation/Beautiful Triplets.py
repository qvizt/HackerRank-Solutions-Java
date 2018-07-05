# Solution for Beautiful Triplets
#
# NOTE: This solutions is possible because it is
# guaranteed that the numbers in the sequence are in
# increasing order. If that is not the case, this solution
# is not going to work - An index-based solution is required
# if that is the case!

def count_triplets(numbers, difference):
    count = 0

    for nr in numbers:
        if nr + difference in numbers:
            if nr + difference + difference in numbers:
                count += 1

    return count


if __name__ == '__main__':
    length, difference = map(int, input().split())
    numbers = set(map(int, input().split()))

    result = count_triplets(numbers, difference)
    print(result)
