# Solution for Validating and Parsing Email Addresses

import re
import email.utils

if __name__ == '__main__':
    n = int(input())

    email_regex = r"^[a-z][\w.-]*@[a-z]+\.[a-z]{1,3}$"
    pattern = re.compile(email_regex, re.I)

    for i in range(n):
        s = input()
        data = email.utils.parseaddr(s)
        if pattern.search(data[1]):
            print(email.utils.formataddr(data))
