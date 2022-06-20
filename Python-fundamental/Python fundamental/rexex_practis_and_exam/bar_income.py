import re

command = input()
total_money = 0

while not command == "end of shift":
    pattern = r"%(?P<name>[A-Z][a-z]+)%<(?P<product>[A-Za-z]+)>[A-z]*\|(?P<quantity>\d+)\|[A-z]*(?P<price>\d+(\.\d)*)\$"
    income = re.finditer(pattern, command)
    for i in income:
        name = i.group("name")
        product = i.group("product")
        price = float(i.group("price")) * float(i.group("quantity"))
        print(f"{name}: {product} - {price:.2f}")
        total_money += price
    command = input()
print(f"Total income: {total_money:.2f}")