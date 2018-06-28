# Solution for Picking Numbers

def longest_selection(numbers):
    numbers.sort()

    selection_start_number = numbers[0]
    next_greater_number_index = 1
    current_selection_length = 1
    longest_selection_length = 1

    for i in range(1, len(numbers)):
        current_number = numbers[i]
        difference = current_number - selection_start_number

        if difference <= 1:
            current_selection_length += 1
            longest_selection_length = max(longest_selection_length, current_selection_length)
            if difference == 1 and current_number != numbers[next_greater_number_index]:
                next_greater_number_index = i
        else:
            selection_start_number = current_number
            next_greater_number_index = i + 1
            current_selection_length = 1

    return longest_selection_length


if __name__ == '__main__':
    input()  # n not required
    numbers = list(map(int, input().split()))
    result = longest_selection(numbers)
    print(result)
