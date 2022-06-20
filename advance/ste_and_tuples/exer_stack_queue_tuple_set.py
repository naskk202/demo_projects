# 1. numbers

# first = set(int(i) for i in input().split())
# second = set(int(i) for i in input().split())
#
# for _ in range(int(input())):
#     command = input().split()
#     if command[0] == "Check":
#         if first.issubset(second) or second.issubset(first):
#             print(True)
#         else:
#             print(False)
#     else:
#         command_nums = set(int(i) for i in command[2:])
#         if command[0] == "Add":
#             if command[1] == "First":
#                 first = first.union(command_nums)
#             else:
#                 second = second.union(command_nums)
#         elif command[0] == "Remove":
#             if command[1] == "First":
#                 first = first.difference(command_nums)
#             else:
#                 second = second.difference(command_nums)
# print(", ".join(str(i) for i in sorted(first)))
# print(", ".join(str(i) for i in sorted(second)))
#
#
#
# a = {2, 3, 5, 6, 8, 9, 19}
# b = {2, 6}
# g = {3, 1}
# c = b.union(g)
# print(c)


# 2. expression_evaluator

# sentences = input().split()
# numbers = []
# result = int(sentences[0])
# sentences.remove(sentences[0])
#
# for i in sentences:
#     if i.lstrip().replace("-", "").isdigit():
#         numbers.append(i)
#     else:
#         numbers.insert(0, str(result))
#         result = int(eval(f"{i}".join(numbers)))
#         numbers.clear()
# print(result)


# 3. milkshake
# from collections import deque
#
# chocolate = [int(i) for i in input().split(", ")]
# cups_of_milk = deque(int(i) for i in input().split(", "))
#
# shake = 0
# choco = chocolate[-1]
# milk = cups_of_milk[0]
# while chocolate and cups_of_milk:
#     while choco < 1 and chocolate:
#         chocolate.pop()
#         if chocolate:
#             choco = chocolate[-1]
#     while milk < 1 and cups_of_milk:
#         cups_of_milk.popleft()
#         if cups_of_milk:
#             milk = cups_of_milk[0]
#     if choco == milk:
#         chocolate.pop()
#         cups_of_milk.popleft()
#         if chocolate:
#             choco = chocolate[-1]
#         if cups_of_milk:
#             milk = cups_of_milk[0]
#         shake += 1
#         if shake == 5:
#             break
#     else:
#         choco -= 5
#         cups_of_milk.append(milk)
#         cups_of_milk.popleft()
#         milk = cups_of_milk[0]
#
# if shake == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
# if chocolate:
#     print(f"Chocolate: {', '.join(str(i) for i in chocolate)}")
# else:
#     print("Chocolate: empty")
# if cups_of_milk:
#     print(f"Milk: {', '.join(str(i) for i in cups_of_milk)}")
# else:
#     print("Milk: empty")

#--------------------------------------------------------------

# from collections import deque
#
# chocolate = [int(i) for i in input().split(", ")]
# cups_milk = deque(int(i) for i in input().split(", "))
#
# shakes = 0
#
# while chocolate and cups_milk and shakes < 5:
#     choco = chocolate.pop()
#     cup = cups_milk.popleft()
#     if choco < 1 and cup < 1:
#         continue
#     if choco < 1:
#         cups_milk.appendleft(cup)
#         continue
#     if cup < 1:
#         chocolate.append(choco)
#         continue
#     if choco == cup:
#         shakes += 1
#     else:
#         chocolate.append(choco - 5)
#         cups_milk.append(cup)
#
# if shakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
# if chocolate:
#     print(f"Chocolate: {', '.join(str(i) for i in chocolate)}")
# else:
#     print("Chocolate: empty")
# if cups_milk:
#     print(f"Milk: {', '.join(str(i) for i in cups_milk)}")
# else:
#     print("Milk: empty")
#

# 4. honey
# from collections import deque
#
# bees = deque(int(i) for i in input().split())
# nectar = [int(i) for i in input().split()]
# symbols = deque(input().split())
#
# honey_made = 0
# nectar_collected = []
#
# while bees and nectar:
#     bee = bees.popleft()
#     current_nectar = nectar.pop()
#     if current_nectar >= bee:
#         sign = symbols.popleft()
#         if sign == "+":
#             honey_made += abs(bee + current_nectar)
#         elif sign == "-":
#             honey_made += abs(bee - current_nectar)
#         elif sign == "*":
#             honey_made += abs(bee * current_nectar)
#         elif sign == "/" and current_nectar > 0:
#             honey_made += abs(bee / current_nectar)
#     else:
#         bees.appendleft(bee)
# print(f"Total honey made: {honey_made}")
# if bees:
#     print(f"Bees left: {', '.join(str(i) for i in bees)}")
# if nectar:
#     print(f"Nectar left: {', '.join(str(i) for i in nectar)}")

# 5. santa_present_factory

# from collections import deque
#
# materials = [int(i) for i in input().split()]
# magick = deque(int(i) for i in input().split())
#
# presents = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
#
# collected_presents = {}
# first_pari = {"Doll", "Wooden train"}
# second_pari = {"Teddy bear", "Bicycle"}
#
#
# while materials and magick:
#     current_materials = materials.pop()
#     current_magick = magick.popleft()
#     pair = current_magick * current_materials
#
#     if current_materials == 0 and current_magick == 0:
#         continue
#     if current_materials == 0:
#         magick.appendleft(current_magick)
#         continue
#     if current_magick == 0:
#         materials.append(current_materials)
#         continue
#
#     if pair < 0:
#         materials.append(current_materials + current_magick)
#
#     elif pair in presents:
#         if presents[pair] not in collected_presents:
#             collected_presents[presents[pair]] = 0
#         collected_presents[presents[pair]] += 1
#
#     elif pair > 0:
#         materials.append(current_materials + 15)
#
# if first_pari.issubset(collected_presents) or second_pari.issubset(collected_presents):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# if materials:
#     print(f"Materials left: {(', '.join(str(i) for i in reversed(materials)))}")
# if magick:
#     print(f"Magic left: {', '.join(str(i) for i in magick)}")
# for k, v in sorted(collected_presents.items()):
#     print(f"{k}: {v}")


# 6. paint_colors
from collections import deque

colors = deque(input().split())
main_colors = []
all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors_combination = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

while colors:
    one = colors.popleft()
    two = colors.pop() if colors else ""
    combo_one, combo_two = (one + two), (two + one)
    if combo_one in all_colors:
        main_colors.append(combo_one)
    elif combo_two in all_colors:
        main_colors.append(combo_two)
    else:
        one = one[:-1]
        two = two[:-1]
        if one:
            colors.insert(len(colors) // 2, one)
        if two:
            colors.insert(len(colors) // 2, two)

for color in main_colors:
    if color in secondary_colors_combination.keys():
        if not secondary_colors_combination[color].issubset(main_colors):
            main_colors.remove(color)
print(main_colors)



# secondary_colors_combination = {
#     "orange": {"red", "yellow"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"}
# }
#
# a, c = "dre", "red"
# b = {"red", "yellow", "dark", "pink"}
# # check for main color in colors
# if a in b or c in b:
#     print(True)
# else:
#     print(False)
# # check for does two secondary colors contain in main colors
# h = "orange"
# if secondary_colors_combination[h].issubset(b):
#     print(True)
# else:
#     print(False)
# # che for secondary colors
# if h in secondary_colors_combination.keys():
#     print(True)
# else:
#     print(False)