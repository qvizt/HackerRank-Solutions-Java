# Solution for Day 26 Nested Logic

from datetime import date


def calculateFine(actual_date, expected_date):
    fine = 0
    if actual_date > expected_date:
        if (actual_date.year > expected_date.year):
            fine = 10000
        elif actual_date.month > expected_date.month:
            fine = 500 * (actual_date.month - expected_date.month)
        elif actual_date.day > expected_date.day:
            fine = 15 * (actual_date.day - expected_date.day)
    return fine


actual_str = input()
expected_str = input()

actual_split = list(map(int, actual_str.split(" ")))
expected_split = list(map(int, expected_str.split(" ")))

actual_date = date(actual_split[2], actual_split[1], actual_split[0])
expected_date = date(expected_split[2], expected_split[1], expected_split[0])

fine = calculateFine(actual_date, expected_date)
print(fine)
