# Solution for Word Order

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    ordered_dictionary = OrderedDict()

    for i in range(n):
        word = input()
        if ordered_dictionary.get(word):
            ordered_dictionary[word] += 1
        else:
            ordered_dictionary[word] = 1

    print(len(ordered_dictionary))
    print(*ordered_dictionary.values())
