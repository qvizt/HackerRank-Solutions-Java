# Solution for Caesar Cipher


def get_encrypted_string(string, rotation_factor):
    encrypted_chars = []
    for char in string:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            ordinal = ord(char) - offset
            ordinal = ordinal + rotation_factor
            ordinal = ordinal % 26
            ordinal = ordinal + offset
            char = chr(ordinal)

        encrypted_chars.append(char)

    return "".join(encrypted_chars)


if __name__ == '__main__':
    input()  # length not required
    string = input()
    rotation_factor = int(input())

    result = get_encrypted_string(string, rotation_factor)
    print(result)
