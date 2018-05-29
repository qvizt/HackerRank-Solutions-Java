# Solution for Re.findall() & Re.finditer()

import re

if __name__ == '__main__':
    s = input()
    regex = r"(?<=[b-df-hj-np-tv-z])[aeiuo]{2,}(?=[b-df-hj-np-tv-z])"
    pattern = re.compile(regex, re.I)
    match = re.findall(pattern, s)
    if match:
        print(*match, sep="\n")
    else:
        print(-1)
