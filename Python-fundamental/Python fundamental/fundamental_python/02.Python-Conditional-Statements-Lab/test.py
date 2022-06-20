vacantion_price = float(input())
puzzle = float(input())
dog = float(input())
bear = float(input())
minion = float(input())
truck = float(input())
puzzle_price = puzzle * 2.6
dog_price = dog * 3
bear_price = bear * 4.1
minion_price = minion * 8.2
truck_price = truck * 2
number_of_toys = puzzle + dog + bear + minion + truck
sum_price = puzzle_price + dog_price + bear_price + minion_price + truck_price
small_order = sum_price * 0.9
big_order = (sum_price * 0.75) * 0.9
if number_of_toys >= 50 and vacantion_price <= big_order:
    print(f"Yes! {big_order - vacantion_price:. 2f} lv left.")
elif number_of_toys >= 50 and vacantion_price > big_order:
    print(f"Not enough money! {vacantion_price - big_order:. 2f} lv needed.")
elif number_of_toys < 50 and vacantion_price <= small_order:
    print(f"Yes! {small_order - vacantion_price:. 2f} lv left.")
elif number_of_toys < 50 and vacantion_price > small_order:
    print(f"Not enough money! {vacantion_price - small_order:. 2f} lv needed.")