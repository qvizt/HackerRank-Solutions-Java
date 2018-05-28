# Solution for Map and Lambda Function

cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    fibo_nr = [0, 1]
    for i in range(2, n + 1):
        fibo = fibo_nr[i - 2] + fibo_nr[i - 1]
        fibo_nr.append(fibo)
    return fibo_nr[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
