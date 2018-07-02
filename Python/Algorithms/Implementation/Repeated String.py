# Solution for Repeated String
import math


def count_a(string, nr_letters):
    count = 0
    if nr_letters <= len(string):
        string = string[:nr_letters]
        count = string.count('a')
    else:
        a_in_string = string.count('a')
        repetitions, remainder = divmod(nr_letters, len(string))
        count = repetitions * a_in_string
        count += string[:remainder].count('a')

    return count


if __name__ == '__main__':
    string = input()
    nr_letters = int(input())

    result = count_a(string, nr_letters)
    print(result)
