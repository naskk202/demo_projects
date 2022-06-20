temperature = float(input())
part_of_the_day = input()
if part_of_the_day == 'Morning' and 18 < temperature <=24 or part_of_the_day == "Afternoon" and 10 <= temperature <= 18 or part_of_the_day == "Evening":
    print(f"It's {int(temperature)} degrees, get your Shirt and Moccasins.")
elif part_of_the_day == 'Morning' and 10 <= temperature <= 18:
    print(f"It's {int(temperature)} degrees, get your Sweatshirt and Sneakers.")
elif part_of_the_day == "Morning" and temperature > 24 or part_of_the_day == "Afternoon" and 18 < temperature <= 24:
    print(f"It's {int(temperature)} degrees, get your T-Shirt and Sandals.")
elif part_of_the_day == "Afternoon" and temperature > 24:
    print(f"It's {int(temperature)} degrees, get your Swim Suit and Barefoot.")