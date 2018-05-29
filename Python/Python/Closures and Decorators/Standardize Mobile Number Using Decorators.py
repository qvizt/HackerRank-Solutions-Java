# Solution for Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            entry = l[i]
            entry = entry[len(entry) - 10::1]
            entry = "+91 " + entry[0:5] + " " + entry[5:]
            l[i] = entry

        return f(l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
