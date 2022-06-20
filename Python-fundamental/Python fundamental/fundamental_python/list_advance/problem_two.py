def if_exist(list_items, item):
    if item in list_items:
        return True
    return False


shopping_list = input().split("!")
command = input()
while not command == "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        if not if_exist(shopping_list, command[1]):
            shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if if_exist(shopping_list, command[1]):
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        if if_exist(shopping_list, command[1]):
            shopping_list = [i if not i == command[1] else command[2] for i in shopping_list]
    elif command[0] == "Rearrange":
        if if_exist(shopping_list, command[1]):
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
    command = input()
print(*shopping_list, sep=", ")
