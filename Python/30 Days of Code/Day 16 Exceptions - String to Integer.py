# Solution for Day 16 Exceptions - String to Integer

# !/bin/python3

import sys

S = input().strip()

try:
    int_value = int(S)
    print(int_value)
except ValueError:
    print("Bad String")
