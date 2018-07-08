# Solution for Cavity Map


def cavity_map(matrix):
    dimension = len(matrix)

    for i in range(1, dimension - 1):
        k = 1
        while k < dimension - 1:
            if matrix[i - 1][k] < matrix[i][k] and \
                    matrix[i][k + 1] < matrix[i][k] and \
                    matrix[i + 1][k] < matrix[i][k] and \
                    matrix[i][k - 1] < matrix[i][k]:
                matrix[i][k] = 'X'
                k += 2
            else:
                k += 1

    return matrix


if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(input())
        matrix.append(row)

    result = cavity_map(matrix)
    for r in result:
        print("".join(r))
