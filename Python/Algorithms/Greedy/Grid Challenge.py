# Solution for Grid Challenge


def are_columns_in_ascending_order(grid):
    n = len(grid)
    in_order = 'YES'

    # first (top) row is nr 0
    r = 0  # rows
    while r < n - 1 and in_order == 'YES':
        upper_row = grid[r]
        lower_row = grid[r + 1]
        for c in range(len(upper_row)):  # columns
            if upper_row[c] > lower_row[c]:
                in_order = 'NO'
                break
        r += 1

    return in_order


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        n = int(input())
        grid = []
        for i in range(n):
            row = [x for x in input()]
            row.sort()
            grid.append(row)

        in_order = are_columns_in_ascending_order(grid)
        print(in_order)
