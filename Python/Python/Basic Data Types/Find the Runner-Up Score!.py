# Solution for Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)

    maximum = arr[0]
    runner_up = None

    for i in arr:
        if i < maximum:
            runner_up = i
            break

    print(runner_up)
