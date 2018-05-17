# Solution for Day 11 2D Arrays

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = 9 * -9  # lowest possible value
    for i in range(4):
        for k in range(4):
            top_sum = sum(arr[i][k:k + 3])
            mid = arr[i + 1][k + 1]
            bot_sum = sum(arr[i + 2][k:k + 3])
            current_sum = top_sum + mid + bot_sum
            max_sum = max(max_sum, current_sum)

    print(max_sum)
