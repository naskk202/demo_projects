products = input().split("|")
budget = int(input())
profit = 0
all_money = 0
for item in products:
    item = item.split("->")
    product = item[0]
    price = float(item[1])
    buy = False
    if product == "Clothes":
        if 0 < price <= 50:
            buy = True
    elif product == "Shoes":
        if 0 < price <= 35:
            buy = True
    elif product == "Accessories":
        if 0 < price <= 20.50:
            buy = True
    if buy:
        if budget >= price:
            budget -= price
            print(f"{price * 1.4:.2f}", end = " ")
            profit += price * 0.4
            all_money += price * 1.4
all_money = all_money + budget
print()
print(f"Profit: {profit:.2f}")
if all_money >= 150:
    print("Hello, France!")
else:
    print("Time to go.")