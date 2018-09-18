# Take N number of commands with args to be executed on an empty list
N = int(input())

number_list = []

for _ in range(N):
    command_with_args = input().split()
    command = command_with_args[0]
    args = command_with_args[1:]
    if command != "print":
        command += "(" + ",".join(args) + ")"
        eval("number_list." + command)
    else:
        print(number_list)
