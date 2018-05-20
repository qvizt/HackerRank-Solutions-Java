# Solution for Designer Door Mat


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    WELCOME_index = n // 2
    door_mat = [None] * n

    for i in range(0, WELCOME_index):
        line = (".|." * (2 * i + 1)).center(m, "-")
        door_mat[i] = line
        door_mat[- i - 1] = line

    door_mat[WELCOME_index] = "WELCOME".center(m, "-")

    for line in door_mat:
        print(line)
