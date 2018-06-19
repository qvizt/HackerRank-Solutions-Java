# Solution for Apple and Orange


def count_fruits_on_house(tree, fruit_distances, *house):
    count = 0
    for f in fruit_distances:
        position = tree + f
        if house[0] <= position <= house[1]:
            count += 1

    return count


if __name__ == '__main__':
    s, t = map(int, input().split())  # house location
    a, b = map(int, input().split())  # apple tree and orange tree
    m, n = map(int, input().split())  # number of apples and oranges
    apples = map(int, input().split())  # distances of the apples
    oranges = map(int, input().split())  # distances of the oranges

    apples_count = count_fruits_on_house(a, apples, s, t)
    oranges_count = count_fruits_on_house(b, oranges, s, t)

    print(apples_count)
    print(oranges_count)
