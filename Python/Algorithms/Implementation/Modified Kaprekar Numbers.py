# Solution for Modified Kaprekar Numbers

def kaprekar_numbers(lower_limit, upper_limit):
    numbers = []

    for i in range(lower_limit, upper_limit + 1):
        square = i * i
        square_str = str(square)
        split_index = len(square_str) // 2
        left = square_str[0:split_index]
        right = square_str[split_index:]
        left = int(left) if len(left) > 0 else 0
        right = int(right) if len(right) > 0 else 0

        if (left + right) == i:
            numbers.append(i)

    return numbers


if __name__ == '__main__':
    lower_limit = int(input())
    upper_limit = int(input())

    result = kaprekar_numbers(lower_limit, upper_limit)
    if len(result) > 0:
        print(" ".join(map(str, result)))
    else:
        print("INVALID RANGE")
