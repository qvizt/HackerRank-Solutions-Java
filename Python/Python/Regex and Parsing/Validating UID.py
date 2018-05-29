# Solution for Validating UID

import re

"""
Splitting the challenge in several tasks.
Just picturing the most important steps.

[0]
Prepare the regex based on the knowledge that the symbols in the
string will be in ascending order.

[1]
Read the string.

[2]
Check the length of the string - must be 10. If the length is not
correct, go to 10.

[3]
Sort the string - simplifies the writing of the regex (See [0].

[4]
Join the string.

[5]
Apply the various regex to get a result.

[6]
Print the result.
"""

if __name__ == '__main__':
    n = int(input())

    # Order of symbols in a sorted string:
    # numbers
    # upper chars, like B, s ...
    # lower chars, like a, e ...
    #
    # Sorted string starts with at least 3 digits,
    # then at least 2 upper chars,
    # then any lower chars
    # and the last check is the length (exactly 10)
    base_regex = r"[0-9]{3,}[A-Z]{2,}[a-z]*"
    base_pattern = re.compile(base_regex)

    duplicate_regex = r"(.)\1"
    duplicate_pattern = re.compile(duplicate_regex)

    for i in range(n):
        result = "Invalid"
        s = input()
        if len(s) == 10:
            s = sorted(s)
            s = "".join(s)

            if base_pattern.search(s):
                if not duplicate_pattern.search(s):
                    result = "Valid"

        print(result)
