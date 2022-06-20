# command = input()
# products = {}
# while not command == "buy":
#     order = command.split()
#     product = order[0]
#     price_quan = [float(order[1]), float(order[2])]
#     if product not in products:
#         products[product] = []
#         products[product] = price_quan
#     else:
#         products[product][0] = price_quan[0]
#         products[product][1] += price_quan[1]
#     command = input()
#
# for k, v in products.items():
#     print(f"{k} -> {(v[0]) * v[1]:.2f}")


command = input()
products = {}

while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

    command = input()
for k, v in products.items():
    print(f"{k} -> {v['price'] * v['quantity']:.2f}")