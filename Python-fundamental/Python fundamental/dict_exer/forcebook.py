# def in_it(my_dict, name):
#     for v in my_dict.values():
#         if name in v:
#             return True
#     return False
#
#
# command = input()
# my_dict = {}
# while not command == "Lumpawaroo":
#     if "|" in command:
#         side, name = command.split(" | ")
#         if in_it(my_dict, name):
#             command = input()
#             continue
#         if side not in my_dict.keys():
#             my_dict[side] = []
#         my_dict[side].append(name)
#     elif "->" in command:
#         name, side = command.split(" -> ")
#         if in_it(my_dict, name):
#             for k, v in my_dict.items():
#                 if name in v:
#                     my_dict[k].remove(name)
#                     if len(my_dict[k]) == 0:
#                         my_dict.pop(k)
#                         break
#             if side not in my_dict.keys():
#                 my_dict[side] = []
#             my_dict[side].append(name)
#             print(f"{name} joins the {side} side!")
#             command = input()
#             continue
#         elif side not in my_dict.keys():
#             my_dict[side] = []
#         print(f"{name} joins the {side} side!")
#         my_dict[side].append(name)
#     command = input()
# for k, v in my_dict.items():
#     my_dict[k] = sorted(v)
# sorted_dict = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))
#
# for k, v in sorted_dict:
#     print(f"Side: {k}, Members: {len(v)}")
#     for i in v:
#         print(f"! {i}")


def in_it(my_dict, name):
    for v in my_dict.values():
        if name in v:
            return True
    return False


command = input()
sides = {}

while not command == "Lumpawaroo":
    if "|" in command:
        side, name = command.split(" | ")
        if not in_it(sides, name):
            if side not in sides:
                sides[side] = []
            sides[side].append(name)
    elif "->" in command:
        name, side = command.split(" -> ")
        if side not in sides:
            sides[side] = []
        elif in_it(sides, name):
            for k, v in sides.items():
                if name in v:
                    sides[k].remove(name)
        print(f"{name} joins the {side} side!")
        sides[side].append(name)
    command = input()

for k, v in sides.items():
     sides[k] = sorted(v)

sorted_dict = sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]))
for k, v in sorted_dict:
    if not len(sides[k]) == 0:
        print(f"Side: {k}, Members: {len(v)}")
        for i in v:
            print(f"! {i}")
