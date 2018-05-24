# Solution for Time Delta

from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    # Sun 10 May 2015 13:54:36 -0700
    format_string = "%a %d %b %Y %X %z"
    t1_datetime = datetime.strptime(t1, format_string)
    t2_datetime = datetime.strptime(t2, format_string)
    delta_seconds = abs(round((t1_datetime - t2_datetime).total_seconds()))
    return delta_seconds


# had to rework the main, otherwise it would not run in PyCharm
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
