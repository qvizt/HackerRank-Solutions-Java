# Solution for Forming a Magic Square

# Useful link with information:
# http://www.math.wichita.edu/~richardson/mathematics/magic%20squares/order3magicsquare.html

def minimum_cost(matrix):
    squares = _magic_squares()
    min_cost = 45

    for s in squares:
        current_cost = 0

        # matrix is n x n, same for each square
        for i in range(len(matrix)):
            for k in range(len(matrix)):
                abs_difference = abs(matrix[i][k] - s[i][k])
                current_cost += abs_difference
        min_cost = min(min_cost, current_cost)

    return min_cost


def _magic_squares():
    magic_squares = []

    # base square is the lo shu magic square
    square = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]

    # base square and its three rotations
    magic_squares.append(square)
    for _ in range(3):
        square = [x.copy() for x in square]
        _left_rotation(square)
        magic_squares.append(square)

    # the reflected versions of each square
    for i in range(len(magic_squares)):
        square = [x.copy() for x in magic_squares[i]]
        _reflect_at_center_column(square)
        magic_squares.append(square)

    return magic_squares


def _left_rotation(square):
    square[0][0], square[0][2], square[2][2], square[2][0] = \
        square[0][2], square[2][2], square[2][0], square[0][0]

    square[0][1], square[1][2], square[2][1], square[1][0] = \
        square[1][2], square[2][1], square[1][0], square[0][1]


def _reflect_at_center_column(square):
    square[0][0], square[0][2] = square[0][2], square[0][0]
    square[1][0], square[1][2] = square[1][2], square[1][0]
    square[2][0], square[2][2] = square[2][2], square[2][0]


if __name__ == '__main__':
    matrix = []

    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)

    cost = minimum_cost(matrix)
    print(cost)
