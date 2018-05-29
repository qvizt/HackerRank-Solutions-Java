# Solution for Group(), Groups() & Groupdict()

# Backreference: https://docs.microsoft.com/en-us/dotnet/standard/base-types/backreference-constructs-in-regular-expressions

import re

if __name__ == '__main__':
    s = input()
    regex = r"([a-zA-Z0-9])\1"
    pattern = re.compile(regex)
    match = re.search(regex, s)

    if match:
        print(match.group(1))
    else:
        print(-1)
