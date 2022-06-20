def stock_availability(*args):
    items = args[0]
    command = args[1]
    if command == "delivery":
        for el in args[2:]:
            items.append(el)
        return items
    elif command == "sell":
        if len(args) == 2:
            return items[1:]
        elif type(args[2]) == int:
            for el in range(int(args[2])):
                if items:
                    items.pop(0)
            return items
        else:
            for el in args[2:]:
                while el in items:
                    items.remove(el)
            return items



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
