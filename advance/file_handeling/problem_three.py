import os

while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    action = command[0]
    file_name = command[1]
    if action == "Create":
        open(file_name, "w")
    elif action == "Add":
        content = command[2]
        if not os.path.exists(file_name):
            open(file_name, "w")
        with open(file_name, "a") as file:
            file.write(f"{content}\n")
    elif action == "Replace":
        old_text, new_text = command[2], command[3]
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            with open(file_name, "r+") as file:
                content = file.read().replace(old_text, new_text)
                file.seek(0)
                file.truncate()
                file.write(content)
    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
