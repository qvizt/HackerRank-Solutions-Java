# Solution for Hex Color Code

import re

if __name__ == '__main__':
    # (?<!^) translates to "not at the start of the string"
    regex = r"(?<!^)(#([a-f0-9]{6}|[a-f0-9]{3}))"
    pattern = re.compile(regex, re.I)

    n = int(input())

    for i in range(n):
        line = input()
        match = pattern.findall(line)
        for m in match:
            print(m[0], sep="\n")
