# Solution for Big Sorting


if __name__ == '__main__':
    n = int(input())
    integers = []

    for _ in range(n):
        integers.append(input())

    integers.sort(key=int)

    for i in integers:
        print(i)
