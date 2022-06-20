nums = input().split()
str = input()
rdy = ""
number = 0
for i in nums:
    for y in i:
        number += int(y)
    for c in range(len(str)):
        while number > len(str):
            number -= len(str)
        else:
            rdy += str[number]
            str = str[:number] + str[number + 1:]
            number = 0
            break
print(rdy)