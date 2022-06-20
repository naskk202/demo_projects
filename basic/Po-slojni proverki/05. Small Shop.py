product = input()
town = input()
number = float(input())
coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0
if town == "Sofia":
    coffee += 0.5
    water += 0.8
    beer += 1.2
    sweets += 1.45
    peanuts += 1.6
elif town == "Plovdiv":
    coffee += 0.4
    water += 0.7
    beer += 1.15
    sweets += 1.3
    peanuts += 1.5
elif town == "Varna":
    coffee += 0.45
    water += 0.7
    beer += 1.1
    sweets += 1.35
    peanuts += 1.55
if product == "coffee":
    product = coffee
elif product == "water":
    product = water
elif product == "beer":
    product = beer
elif product == "sweets":
    product = sweets
elif product == "peanuts":
    product = peanuts
sum = number * product
print(sum)




product = input()
town = input()
number = float(input())
price = 0
if town == "Sofia":
    if product == "coffee":
        price = 0.5
    elif product == "water":
        price = 0.8
    elif product == "beer":
        price = 1.2
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.6
elif town == "Plovdiv":
    if product == "coffee":
        price = 0.4
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.3
    elif product == "peanuts":
        price = 1.5
elif town == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.1
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
sum = price * number
print(sum)