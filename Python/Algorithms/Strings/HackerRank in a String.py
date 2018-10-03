# Solution for HackerRank in a String


def string_contains_hackkerank(string):
    hackerrank = "hackerrank"
    hr_length = len(hackerrank)
    index = 0

    for c in string:
        if c == hackerrank[index]:
            index += 1
            if index == hr_length:
                break

    return "YES" if index == hr_length else "NO"


if __name__ == '__main__':
    nr_queries = int(input())

    for i in range(0, nr_queries):
        string = input()

        result = string_contains_hackkerank(string)
        print(result)
