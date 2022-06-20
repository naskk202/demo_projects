plan_gifts = input().split(" ")
gift = input()
while not gift == "No Money":
    gift = gift.split(" ")
    if "OutOfStock" in gift:
        for missing in range(len(plan_gifts)):
            if gift[1] == plan_gifts[missing]:
                plan_gifts[missing] = "None"
    elif "Required" in gift:
        if 0 < int(gift[2]) < len(plan_gifts):
            plan_gifts[int(gift[2])] = gift[1]
    elif "JustInCase" in gift:
        plan_gifts[-1] = gift[1]
    gift = input()
while "None" in plan_gifts:
    plan_gifts.remove("None")
for i in plan_gifts:
    print(i, end = " ")