# Solution for Pangrams


def check_pangram_status(string):
    unique_characters = set()
    for c in string:
        if not c.isspace():
            unique_characters.add(c.lower())

    return "pangram" if len(unique_characters) == 26 else "not pangram"


if __name__ == '__main__':
    string = input()

    result = check_pangram_status(string)
    print(result)
