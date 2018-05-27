# Solution for Athlete Sort

if __name__ == '__main__':
    n, m = map(int, input().split())

    data = [list(map(int, input().split())) for i in range(n)]

    k = int(input())

    data.sort(key=lambda x: x[k])

    for i in range(n):
        print(*data[i])
