# Solution for List Comprehensions


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[x_val, y_val, z_val] for x_val in range(x + 1) for y_val in range(y + 1) for z_val in range(z + 1) if
              x_val + y_val + z_val != n]
    print(result)