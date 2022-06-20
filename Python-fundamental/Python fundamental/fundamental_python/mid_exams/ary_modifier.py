array = input().split()
command = input()

while not command == "end":
    action = command.split()
    if action[0] == "swap":
        array[int(action[1])], array[int(action[2])] = array[int(action[2])], array[int(action[1])]
    elif action[0] == "multiply":
        array[int(action[1])] = str(int(array[int(action[1])]) * int(array[int(action[2])]))
    elif action[0] == "decrease":
        array = [str(int(i) - 1) for i in array]
    command = input()
print(", ".join(array))