# Solution for Happy Ladybugs


def are_ladybugs_happy(board):
    overview = {}

    for cell in board:
        if overview.get(cell):
            overview[cell] += 1
        else:
            overview[cell] = 1

    if overview.get('_'):
        del overview['_']
        for value in overview.values():
            if value < 2:
                return 'NO'
    else:
        previous = (board[0], 1)  # (color, count)
        for i in range(1, len(board)):
            current = board[i]
            if current == previous[0]:
                previous = (current, previous[1] + 1)
            else:
                if previous[1] == 1:
                    return 'NO'
                else:
                    previous = (current, 1)
        if previous[1] == 1:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    games = int(input())

    for _ in range(games):
        input()  # n not required
        board = input()

        result = are_ladybugs_happy(board)
        print(result)
