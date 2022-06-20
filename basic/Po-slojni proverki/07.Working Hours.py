hour = float(input())
day = input()

if day == "Saturday" or day == "Monday" or day == "Tuesday" or\
        day == "Wednesday" or day == "Thursday" or day == "Friday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")


hour = float(input())
day = input()
is_working_day = day == "Saturday" or day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
is_working_hour = 10 <= hour <= 18
if is_working_day and is_working_hour:
    print("open")
else:
    print("closed")