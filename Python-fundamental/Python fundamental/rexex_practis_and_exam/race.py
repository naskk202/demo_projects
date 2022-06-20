import re

list_of_names = input().split(", ")
command = input()
my_dict = {}

while not command == "end of race":
    name = ""
    distanc = 0
    name_text = re.finditer(r"[A-Z]|[a-z]+", command)
    for i in name_text:
        name += i.group()
    if name in list_of_names:
        km_text = re.finditer(r"\d", command)
        for i in km_text:
            distanc += int(i.group())
        if name not in my_dict:
            my_dict[name] = 0
        my_dict[name] += distanc
    command = input()

sorted_race = sorted(my_dict.items(), key=lambda x: -x[1])
print(f"1st place: {sorted_race[0][0]}")
print(f"2nd place: {sorted_race[1][0]}")
print(f"3rd place: {sorted_race[2][0]}")
