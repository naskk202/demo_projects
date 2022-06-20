text = input()
command = input()

while not command == "Reveal":
    if "InsertSpace" in command:
        index = int(command.split(":|:")[1])
        text = text[:index] + " " + text[index:]
        print(text)
    elif "Reverse" in command:
        substring = command.split(":|:")[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            text = text + substring[::-1]
            print(text)
        else:
            print("error")
    elif "ChangeAll" in command:
        old, new = command.split(":|:")[1], command.split(":|:")[2]
        text = text.replace(old, new)
        print(text)
    command = input()
print(f"You have a new text message: {text}")
