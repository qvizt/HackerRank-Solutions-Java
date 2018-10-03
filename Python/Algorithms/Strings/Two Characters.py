# Solution for Two Characters
import itertools


def get_longest_two_alternating_char_sequence(string):
    max_length = 0

    # Determine all possible combinations with two characters
    char_combinations = list(itertools.combinations(set(string), 2))

    # Check every combination
    for combination in char_combinations:
        update = True
        sequence = []

        # Build string based on two characters and their presence
        # in the string
        for char in string:
            if char in combination:
                sequence.append(char)

        # Check for alternation
        for index in range(0, len(sequence) - 1):
            if sequence[index] == sequence[index + 1]:
                update = False
                break

        if update and max_length < len(sequence):
            max_length = len(sequence)

    return max_length


if __name__ == '__main__':
    input()  # length not required
    string = input()

    result = get_longest_two_alternating_char_sequence(string)
    print(result)
