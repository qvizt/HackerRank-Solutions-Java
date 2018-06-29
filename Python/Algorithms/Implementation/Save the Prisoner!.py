# Solution for Save the Prisoner!


def warn_prisoner(prisoners, sweets, chair):
    p = chair + sweets - 1
    if p > prisoners:
        p = p % prisoners
        if p:
            return p
        return prisoners
    return p


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        prisoners, sweets, chair = map(int, input().split())

        result = warn_prisoner(prisoners, sweets, chair)
        print(result)
