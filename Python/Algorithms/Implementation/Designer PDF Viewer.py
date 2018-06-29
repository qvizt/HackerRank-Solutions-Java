# Solution for Designer PDF Viewer


def area(word, letter_heights):
    letter_ord_difference = ord('a')
    width = len(word)
    height = 0

    for w in word:
        index = ord(w) - letter_ord_difference
        w_height = letter_heights[index]
        height = max(height, w_height)

    a = width * height

    return a


if __name__ == '__main__':
    letter_heights = list(map(int, input().split()))
    word = input()

    result = area(word, letter_heights)
    print(result)
