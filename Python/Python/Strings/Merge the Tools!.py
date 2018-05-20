# Solution for Merge the Tools!


def merge_the_tools(string, k):
    index = 0
    while index < len(string):
        sub = string[index:index + k:]
        index += k

        unique_char_sequence = []
        for c in sub:
            if c not in unique_char_sequence:
                unique_char_sequence.append(c)

        output = "".join(unique_char_sequence)
        print(output)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
