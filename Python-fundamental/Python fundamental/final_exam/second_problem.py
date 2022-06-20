import re
number_of_commands = int(input())
pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[A-Za-z]{8,})\]"
nums = ""

for i in range(number_of_commands):
    text = input()
    encrypted_text = [i.groups() for i in re.finditer(pattern, text)]
    if encrypted_text:
        nums = [str(ord(i)) for i in encrypted_text[0][1]]
        print(f"{encrypted_text[0][0]}: {' '.join(nums)}")
    else:
        print("The message is invalid")