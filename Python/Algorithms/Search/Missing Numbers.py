# Solution for Missing Numbers


def get_missing_numbers(list_missing, list_origin):
    origin_number_count_mapping = {}

    for nr in list_origin:
        count = origin_number_count_mapping.get(nr, 0)
        count = count + 1
        origin_number_count_mapping[nr] = count

    for nr in list_missing:
        count = origin_number_count_mapping[nr]
        count = count - 1
        if count == 0:
            origin_number_count_mapping.pop(nr)
        else:
            origin_number_count_mapping[nr] = count

    missing_numbers = list(origin_number_count_mapping.keys())
    missing_numbers.sort()
    missing_numbers = list(map(str, missing_numbers))

    return ' '.join(missing_numbers)


if __name__ == '__main__':
    input()  # skip n
    list_missing = [int(x) for x in input().split()]
    input()  # skip m
    list_origin = [int(x) for x in input().split()]
    missing_numbers = get_missing_numbers(list_missing, list_origin)
    print(missing_numbers)
