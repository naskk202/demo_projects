import re

command = input()
total_price = 0
print("Bought furniture:")
while not command == "Purchase":
    item = re.finditer(r">>(?P<name>[A-z\da-z]+)<<(?P<price>\d+\.?\d+?)!(?P<amount>\d+)", command)
    for a in item:
        name = a.group("name")
        price = a.group("price")
        amount = a.group("amount")
        print(name)
        total_price += float(price) * float(amount)
    command = input()
print(f"Total money spend: {total_price:.2f}")