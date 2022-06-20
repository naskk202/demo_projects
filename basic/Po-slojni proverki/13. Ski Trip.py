days = int(input())
room = input()
rating = input()
price = 0
if room == "room for one person":
    price = 18
elif room == "apartment":
    if days - 1 < 10:
        price = 25 * 0.7
    elif 10 <= days - 1 <= 15:
        price = 25 * 0.65
    elif days > 15:
        price = 25 * 0.5
elif room == "president apartment":
    if days - 1 < 10:
        price = 35 * 0.9
    elif 10 <= days - 1 <= 15:
        price = 35 * 0.85
    elif days > 15:
        price = 35 * 0.8
if rating == "positive":
    print(f"{(price * (days - 1)) * 1.25:.2f}")
elif rating == "negative":
    print(f"{(price * (days - 1)) * 0.9:.2f}")