# Solution for Time Conversion

# !/bin/python3

import time


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    old_format = "%I:%M:%S%p"
    old_time = time.strptime(s, old_format)

    new_format = "%H:%M:%S"
    result = time.strftime(new_format, old_time)

    return result


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
