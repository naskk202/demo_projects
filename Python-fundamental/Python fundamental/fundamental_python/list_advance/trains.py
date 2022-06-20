train = [0] * int(input())
command = input().split()
while not "End" in command:
    if "add" in command:
        train[-1] += int(command[1])
    elif "insert" in command:
        train[int(command[1])] += int(command[2])
    elif "leave" in command:
        train[int(command[1])] -= int(command[2])
    command = input().split()
print(train)
