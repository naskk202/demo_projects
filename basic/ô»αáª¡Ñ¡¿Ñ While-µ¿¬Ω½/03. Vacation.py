money_needed = float(input())
saved_money = float(input())
days = 0
days_spend = 0
while money_needed > saved_money and days_spend < 5:
    action = input()
    day_money = float(input())
    days += 1
    if action == "spend":
        days_spend += 1
        saved_money -= day_money
        if saved_money < 0:
            saved_money = 0
    else:
        saved_money += day_money
        days_spend = 0
if days_spend == 5:
    print(f"You can't save the money.\n"
          f"{days}")
else:
    print(f"You saved the money for {days} days.")