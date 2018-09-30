# Solution for Strong Password


def additional_characters(password):
    special_characters = "!@#$%^&*()-+"
    has_digit = False
    has_lower = False
    has_upper = False
    has_special_characters = False
    count = 4

    for c in password:
        if c.isdigit() and not has_digit:
            has_digit = True
            count -= 1
        elif c.islower() and not has_lower:
            has_lower = True
            count -= 1
        elif c.isupper() and not has_upper:
            has_upper = True
            count -= 1
        elif c in special_characters and not has_special_characters:
            has_special_characters = True
            count -= 1

    return max(count, 6 - len(password))


if __name__ == '__main__':
    input()  # reading length is not required
    password = input()

    result = additional_characters(password)

    print(result)
