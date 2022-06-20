month = input()
overnight = int(input())
apartment_per_night = 0
studio_per_night = 0
if month == "May" or month == "October":
    studio_per_night = 50
    apartment_per_night = 65
elif month == "June" or month == "September":
    studio_per_night = 75.2
    apartment_per_night = 68.7
elif month == "July" or month == "August":
    studio_per_night = 76
    apartment_per_night = 77
if 13 >= overnight > 7:
    if month == "May" or month == "October":
        studio_per_night = studio_per_night * 0.95
elif overnight > 14:
    if month == "May" or month == "October":
        studio_per_night = studio_per_night * 0.70
    elif month == "June" or month == "September":
        studio_per_night = studio_per_night * 0.80
if overnight > 14:
    apartment_per_night = apartment_per_night * 0.9
print(f"Apartment: {apartment_per_night * overnight:.2f} lv.")
print(f"Studio: {studio_per_night * overnight:.2f} lv.")