hour = int(input())
minutes = int(input())
left = abs(hour-24)
minutes_print = 0
hour_print = 0
if minutes + 15 > 59:
    minutes_print = (minutes +15) - 60
else:
    minutes_print = minutes + 15
if minutes + 15 > 59 and hour == 23:
    hour_print = 0
elif minutes + 15 > 59:
    hour_print = hour + 1
else:
    hour_print = hour
if minutes_print < 10:
    print(f"{hour_print}:0{minutes_print}")
else:
    print(f"{hour_print}:{minutes_print}")
