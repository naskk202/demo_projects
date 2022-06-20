text = input()
command = input()

while not command == "Done":
    command = command.split()
    if "Change" in command:
        old, new = command[1], command[2]
        text = text.replace(old, new)
        print(text)
    elif "Includes" in command:
        if command[1] in text:
            print(True)
        else:
            print(False)
    elif "End" in command:
        if command[1] == text[(len(text) - len(command[1])):]:
            print(True)
        else:
            print(False)
    elif "Uppercase" in command:
        text = text.upper()
        print(text)
    elif "FindIndex" in command:
        print(text.index(command[1]))
    elif "Cut" in command:
        start = int(command[1])
        end = int(command[2]) + int(command[1])
        text = text[start:end]
        print(text)
    command = input()
