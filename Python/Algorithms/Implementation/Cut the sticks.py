# Solution for Cut the sticks


if __name__ == '__main__':
    input()  # n not required
    sticks = list(map(int, input().split()))
    sticks.sort()

    i = 0
    while i < (len(sticks)):
        print(len(sticks) - i)
        current_stick = sticks[i]

        while i < (len(sticks) - 1) and current_stick == sticks[i + 1]:
            i += 1
        else:
            i += 1
