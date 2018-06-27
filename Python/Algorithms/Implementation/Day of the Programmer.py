# Solution for Day of the Programmer
from datetime import date, timedelta


def day_of_the_programmer(year):
    first_day_of_the_year = date(year=year, month=1, day=1)
    days_to_add = 255

    if year < 1918 and year % 4 == 0 and year % 100 == 0:
        days_to_add -= 1
    elif year == 1918:
        days_to_add += 13

    days_delta = timedelta(days=days_to_add)
    day_of_the_programmer = first_day_of_the_year + days_delta

    formatting = "%d.%m.%Y"

    return day_of_the_programmer.strftime(formatting)


if __name__ == '__main__':
    y = int(input())

    day = day_of_the_programmer(y)
    print(day)
