coin_1 = int(input())
coin_2 = int(input())
coin_5 = int(input())
sum = int(input())
for a in range(coin_1 + 1):
    for b in range(coin_2 + 1):
        for c in range(coin_5 + 1):
            if a + (b * 2) + (c * 5) == sum:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {sum} lv.")