# Solution for Mars Exploration


def get_number_of_altered_letters(received_sos):
    nr_of_sos = len(received_sos) // 3
    sos = "SOS" * nr_of_sos
    nr_altered_letters = 0

    for index in range(0, len(received_sos)):
        if received_sos[index] != sos[index]:
            nr_altered_letters += 1

    return nr_altered_letters


if __name__ == '__main__':
    received_sos = input()

    result = get_number_of_altered_letters(received_sos)
    print(result)
