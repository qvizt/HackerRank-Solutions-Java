# Solution for Set .discard(), .remove() & .pop()


if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))

    n = int(input())

    for i in range(n):
        command_line = input()
        split_command = command_line.split()
        command = split_command[0]

        if command == "pop":
            s.pop()
        elif command == "discard":
            s.discard(int(split_command[1]))
        else:
            s.remove(int(split_command[1]))

    print(sum(s))
