# Solution for CamelCase


def count_words(sentence):
    count = 1

    for c in sentence:
        if c.isupper():
            count += 1

    return count


if __name__ == '__main__':
    sentence = input()

    count = count_words(sentence)

    print(count)
