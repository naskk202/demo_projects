budget = float(input())
season = input()
trip_price = 0
destination = 0
sleep_in = 0
if budget > 1000:
    destination = "Europe"
    sleep_in = "Hotel"
    trip_price = budget * 0.9
elif budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip_price = budget * 0.3
        sleep_in = "Camp"
    elif season == "winter":
        trip_price = budget * 0.7
        sleep_in = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip_price = budget * 0.4
        sleep_in = "Camp"
    elif season == "winter":
        trip_price = budget * 0.8
        sleep_in = "Hotel"
print(f"Somewhere in {destination}")
print(f"{sleep_in} - {trip_price:.2f}")