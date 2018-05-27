# Solution for Any or All

if __name__ == '__main__':
    input()  # N not required at all
    string_numbers = input().split()
    if all(int(nr) >= 0 for nr in string_numbers):
        print(any(nr == nr[-1::-1] for nr in string_numbers))
    else:
        print(False)