# Solution for start() & end()

import re

if __name__ == '__main__':
    s = input()
    k = input()

    pattern = re.compile(r"(?=" + k + ")")
    match = list(re.finditer(pattern, s))
    if match:
        for m in match:
            print((m.start(), m.start() + len(k) - 1))
    else:
        print("(-1, -1)")
