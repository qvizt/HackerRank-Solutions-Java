# Solution for String Split and Join

def split_and_join(line):
    split = line.split(" ")
    join = "-".join(split)
    return join


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
