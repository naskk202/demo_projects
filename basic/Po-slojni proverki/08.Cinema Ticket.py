day = input()
if day == "Monday" or day =="Tuesday" or day =="Friday":
    day = 12
elif day == "Wednesday" or day =="Thursday":
    day = 14
elif day == "Saturday" or day =="Sunday":
    day = 16
print(day)