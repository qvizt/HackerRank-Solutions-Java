# Solution for Jumping on the Clouds


def min_jumps(clouds):
    jumps = 0

    index = 0
    while True:
        if index == len(clouds) - 1:
            break

        look_ahead_index = index + 2
        if look_ahead_index < len(clouds) and clouds[look_ahead_index] != 1:
            index = look_ahead_index
        else:
            index += 1

        jumps += 1

    return jumps


if __name__ == '__main__':
    input()  # n not required
    clouds = list(map(int, input().split()))

    result = min_jumps(clouds)
    print(result)
