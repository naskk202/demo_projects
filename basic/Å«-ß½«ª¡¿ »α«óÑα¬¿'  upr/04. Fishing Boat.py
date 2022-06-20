budget = float(input())
season = input()
people = int(input())
boat_rent = 0
boat_price = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600
if people <= 6:
    boat_price = boat_rent * 0.9
elif 7 <= people <= 11:
    boat_price = boat_rent * 0.85
elif people >= 12:
    boat_price = boat_rent * 0.75
if not season == "Autumn":
    if people % 2 == 0:
        boat_price = boat_price * 0.95
if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")