# Solution for Validating Credit Card Numbers

import re

if __name__ == '__main__':

    # 16 digits and correct hyphens (either 0 or 3).
    base_regex = r"^[4-6]\d{3}(-)?\d{4}(?(1)-|)\d{4}(?(1)-|)\d{4}$"
    base_pattern = re.compile(base_regex)

    # four consecutive digits
    consecutive_regex = r"(\d)\1{3}"
    consecutive_pattern = re.compile(consecutive_regex)

    n = int(input())

    for i in range(n):
        card = input()
        result = "Invalid"

        if base_pattern.search(card):
            # Remove hyphens -> simplifies the pattern
            card = re.sub("-", "", card)

            if not consecutive_pattern.search(card):
                result = "Valid"

        print(result)
