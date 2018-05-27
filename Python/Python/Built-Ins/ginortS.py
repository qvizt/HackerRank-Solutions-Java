# Solution for ginortS

if __name__ == '__main__':
    string = input()
    lower = []
    upper = []
    odd = []
    even = []

    for char in string:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.isdigit():
            if int(char) & 1 == 1:
                odd.append(char)
            else:
                even.append(char)

    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()

    result = []
    result.extend(lower)
    result.extend(upper)
    result.extend(odd)
    result.extend(even)
    result = "".join(result)

    print(result)
