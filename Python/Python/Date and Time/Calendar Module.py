# Solution for Calendar Module

import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    weekday_nr = calendar.weekday(year, month, day)
    weekday_string = calendar.day_name[weekday_nr]
    print(weekday_string.upper())
