# Solution for Collections.deque()

import collections

if __name__ == '__main__':
    deque = collections.deque()

    n = int(input())

    for i in range(n):
        split_input = input().split()
        operation = split_input[0]
        args = split_input[1:]
        exec_string = "deque." + operation + "(" + ", ".join(args) + ")"
        exec(exec_string)

    print(*deque)
