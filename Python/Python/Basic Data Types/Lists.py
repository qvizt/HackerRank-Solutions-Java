# Solution for Lists


if __name__ == '__main__':
    N = int(input())

    my_list = []
    for i in range(N):
        command = input()
        split_command = command.split(" ")
        if split_command[0] == "print":
            print(my_list)
        else:
            exec_command = "my_list." + (split_command[0]) + "(" + ", ".join(split_command[1:]) + ")"
            exec(exec_command)
