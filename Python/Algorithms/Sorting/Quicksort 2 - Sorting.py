# Solution for Quicksort 2 - Sorting
# This solution adapts the partition part
# of Quicksort 1 - Partition v2.


def quick_sort(numbers):
    if len(numbers) > 1:
        le = []
        eq = []
        ri = []
        eq.append(numbers[0])

        for i in range(1, len(numbers)):
            if numbers[i] < eq[0]:
                le.append(numbers[i])
            elif numbers[i] > eq[0]:
                ri.append(numbers[i])
            else:
                eq.append(numbers[i])

        quick_sort(le)
        quick_sort(ri)

        i = 0
        for n in le:
            numbers[i] = n
            i += 1

        for n in eq:
            numbers[i] = n
            i += 1

        for n in ri:
            numbers[i] = n
            i += 1

        print(' '.join(map(str, numbers)))


if __name__ == '__main__':
    input()  # skip size
    numbers = list(map(int, input().split()))

    quick_sort(numbers)
