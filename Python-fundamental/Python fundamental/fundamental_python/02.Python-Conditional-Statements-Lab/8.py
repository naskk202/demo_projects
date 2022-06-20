vacation_price = float(input())
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
total_toys = puzzle + dog + bear + minion + truck
total_price = puzzle_price + dog_price + bear_price + minion_price + truck_price
small_order = total_price * 0.9
discount = total_price * 0.75
big_order = discount * 0.9
if total_toys < 50 and vacation_price > small_order:
    print(f"Not enough money! {vacation_price - small_order:.2f} lv needed.")
elif total_toys < 50 and vacation_price <= small_order:
    print(f"Yes! {small_order - vacation_price:.2f} lv left.")
elif total_toys >= 50 and vacation_price <= big_order:
    print(f"Yes! {big_order - vacation_price:.2f} lv left.")
elif total_toys >= 50 and vacation_price > big_order:
    print(f"Not enough money! {vacation_price - big_order:.2f} lv needed.")