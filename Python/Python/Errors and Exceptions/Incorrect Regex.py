# Solution for Incorrect Regex

import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        try:
            s = input()
            pattern = re.compile(s)
            print("True")
        except Exception as e:
            print("False")
