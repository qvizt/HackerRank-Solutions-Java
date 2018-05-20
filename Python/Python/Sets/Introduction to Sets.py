# Solution for Introduction to Sets


def average(array):
    distinct_heights = set(array)
    sum_heights = sum(distinct_heights)
    average = sum_heights / len(distinct_heights)

    return average



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)