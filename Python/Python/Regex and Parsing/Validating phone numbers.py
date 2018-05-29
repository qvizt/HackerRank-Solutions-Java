# Solution for Validating phone numbers

import re

if __name__ == '__main__':
    regex = r"^[7-9][0-9]{9}$"
    pattern = re.compile(regex)

    n = int(input())
    for i in range(n):
        nr = input()
        match = pattern.match(nr)
        print("YES" if match else "NO")
