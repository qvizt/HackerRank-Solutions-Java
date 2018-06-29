# Solution for Circular Array Rotation


def rotate(elements, k):
    copy = elements.copy()
    for i in range(len(copy)):
        index = (i + k) % len(elements)
        elements[index] = copy[i]


if __name__ == '__main__':
    n, rotations, queries = map(int, input().split())
    elements = list(map(int, input().split()))

    rotate(elements, rotations)
    print(elements)

    for _ in range(queries):
        index = int(input())
        print(elements[index])
