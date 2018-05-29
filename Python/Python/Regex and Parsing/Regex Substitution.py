# Solution for Regex Substitution

import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        line = input()
        while " && " in line or " || " in line:
            line = line.replace(" && ", " and ")
            line = line.replace(" || ", " or ")

        print(line)
