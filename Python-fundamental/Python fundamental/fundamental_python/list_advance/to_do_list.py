# command = input().split("-")
# to_do_list = [0] * 10
# while not "End" in command:
#     to_do_list.insert(int(command[0]), command[1])
#     command = input().split("-")
# to_do_list = [i for i in to_do_list if not i == 0]
# print(to_do_list

to_do_list = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    task = command.split("-")
    priority: int = int(task[0])
    note = task[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)
result = [i for i in to_do_list if not i == 0]
print(result)