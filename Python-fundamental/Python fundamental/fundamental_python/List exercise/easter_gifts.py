gifts = input().split()
gif = input()
while not gif == "No Money":
    gif = gif.split()
    if "OutOfStock" in gif:
        for i in range(len(gifts)):
            if gif[1] == gifts[i]:
                gifts[i] = "None"
    if "Required" in gif:
        if 0 <= int(gif[2]) < len(gifts):
            gifts[int(gif[2])] = gif[1]
        else:
            pass
    if "JustInCase" in gif:
        gifts[-1] = gif[1]
    gif = input()
while "None" in gifts: gifts.remove("None")
for i in gifts:
    print(i, end=" ")
