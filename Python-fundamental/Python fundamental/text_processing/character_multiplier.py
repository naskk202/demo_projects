# words = input().split()
# sum = 0
# if len(words[0]) > len(words[1]):
#     one, two = words
# else:
#     two, one = words
# for i in range(len(one)):
#     if not i >= len(two):
#         sum += ord(one[i]) * ord(two[i])
#     else:
#         sum += ord(one[i])
# print(sum)



# directory = input().split('\\')
# file = directory[-1].split(".")
# print(f"File name: {file[0]}")
# print(f"File extension: {file[1]}")



# text = input()
# crypted_tex = ""
# for char in text:
#     crypted_tex += chr(ord(char) + 3)
# print(crypted_tex)

# print("".join([chr(ord(i) + 3) for i in input()]))


# string = input()
# while ":" in string:
#     emote = string.find(":")
#     print(string[emote] + string[emote + 1])
#     string = string.replace(":", "", 1)



# string = input()
# new_string = ""
# for i in range(len(string) - 1):
#     if string[i] == string[i + 1]:
#         continue
#     else:
#         new_string += string[i]
# print(new_string + string[-1])

text = input()
bomb_power = 0
i = 0
result = ""

while i < len(text):
    curr_char = text[i]
    if curr_char == ">":
        result += ">"
        bomb_power += int(text[i + 1])
    else:
        if bomb_power > 0:
            bomb_power -= 1
        else:
            result += curr_char
    i += 1
print(result)