# Solution for Text Wrap

import textwrap


def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    wrapped_joined = " ".join(wrapped)
    filled = textwrap.fill(wrapped_joined, max_width)
    return filled


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
