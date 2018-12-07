# Solution for Beautiful Binary String
import re


def get_nr_of_steps(s):
    p = '010'
    nr = 0
    itr = re.finditer(p, s)

    for _ in itr:
        nr += 1

    return nr


if __name__ == '__main__':
    input()  # length not required
    s = input()
    result = get_nr_of_steps(s)
    print(result)
