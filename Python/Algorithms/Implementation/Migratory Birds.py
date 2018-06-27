# Solution for Migratory Birds
from collections import defaultdict


def determine_most_common_bird(ar):
    birds = defaultdict(int)
    for b in ar:
        birds[b] += 1

    # retrieve the item that returns the max nr of sightings
    most_common_bird = max(birds.items(), key=lambda item: item[1])

    # return the first index (= nr of the bird)
    return most_common_bird[0]


if __name__ == '__main__':
    input()  # n not required
    ar = list(map(int, input().split()))  # type numbers

    most_common_bird = determine_most_common_bird(ar)
    print(most_common_bird)
