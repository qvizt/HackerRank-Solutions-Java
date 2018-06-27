# Solution for Cats and a Mouse


def get_winner(a, b, c):
    distance_a_c = distance(a, c)
    distance_b_c = distance(b, c)

    if distance_a_c < distance_b_c:
        winner = 'Cat A'
    elif distance_b_c < distance_a_c:
        winner = 'Cat B'
    else:
        winner = 'Mouse C'

    return winner


def distance(x, y):
    return abs(x - y)


if __name__ == '__main__':
    q = int(input())

    for i in range(q):
        a, b, c = map(int, input().split())
        winner = get_winner(a, b, c)
        print(winner)
