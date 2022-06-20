collection_of_items = input().split("|")
budget = float(input())
purchase = False
items = []
for item in collection_of_items:
    item = item.split("->")
    if item[0] == "Clothes" and float(item[1]) <= 50:
        purchase = True
    elif item[0] == "Shoes" and float(item[1]) <= 35:
        purchase = True
    elif item[0] == "Accessories" and float(item[1]) <= 20.50:
        purchase = True
    if purchase and budget >= float(item[1]):
        budget -= float(item[1])
        items.append(float(item[1]))
    purchase = False
profit = 0
for price in items:
    new_price = price * 1.4
    budget += new_price
    print(f"{new_price:.2f}", end = " ")
    profit += new_price - price
print()
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")