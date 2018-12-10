# Solution for Counting Sort 2


def get_sorted_array(numbers):
    li = [0] * 100

    for n in numbers:
        li[n] += 1

    sli = []
    for i in range(len(li)):
        for k in range(li[i]):
            sli.append(i)

    return sli


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    result = get_sorted_array(numbers)
    print(' '.join(map(str, result)))
