# Solution for Detect Floating Point Number

import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line = input()
        regex = r"^[+-]?\d*\.\d*$"
        pattern = re.compile(regex)
        match = re.search(pattern, line)

        print(True if match else False)
