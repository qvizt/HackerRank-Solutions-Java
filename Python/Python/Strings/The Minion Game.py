# Solution for The Minion Game


"""
Explaining via the word BANANA for the mathematical part:

Listing for each consonant:
BANANA ("base substring")
BANAN
BANA
BAN
BA
B

NANA ("base substring")
NAN
NA
N

NA ("base substring)
N

You can tell that the number of possible substrings is equal
to the length of the "base substring" that is used to create the substrings.
( See https://en.wikipedia.org/wiki/Substring )

Instead of computing every single substring it is easier and faster
just to add the length of "base substring" and move to the next
character in the string that has been passed as argument.
"""


def minion_game(string):
    length = len(string)
    vowels = "AEIOU"

    kevin_score = 0
    stuart_score = 0

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Stuart", stuart_score)


if __name__ == '__main__':
    s = input()
    minion_game(s)
