# Solution for Angry Professor


def is_cancelled(threshold, arrival_times):
    in_time = 0

    for at in arrival_times:
        if at <= 0:
            in_time += 1

    if in_time < threshold:
        return "YES"

    return "NO"


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        nr_students, threshold = map(int, input().split())
        arrival_times = list(map(int, input().split()))

        result = is_cancelled(threshold, arrival_times)
        print(result)
