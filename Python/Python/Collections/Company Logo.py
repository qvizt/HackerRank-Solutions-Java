# Solution for Company Logo

from collections import Counter

if __name__ == '__main__':
    letters = list(input())
    letter_counter = Counter(letters)
    sorted_items = sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))

    for c in sorted_items[0:3]:
        print(*c)
