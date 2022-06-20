exam_hour = int(input())
exam_minute = int(input())
arive_hour = int(input())
arive_minute = int(input())
exam_time = (exam_hour * 60) + exam_minute
arive_time = (arive_hour * 60) + arive_minute
time = exam_time - arive_time
time_positive = abs(time)
hour = time_positive // 60
minute = time_positive % 60
if exam_hour == arive_hour and exam_minute == arive_minute:
    print("On time")
elif 0 < time <= 30:
    print(f"On time\n"
          f"{minute} minutes before the start")
elif time < 0:
    if hour < 1:
        print(f"Late\n"
              f"{minute} minutes after the start")
    elif hour >= 1 and minute >= 10:
        print(f"Late\n"
              f"{hour}:{minute} hours after the start")
    else:
        print(f"Late\n"
              f"{hour}:0{minute} hours after the start")
elif 30 < time < 60:
    print(f"Early\n"
          f"{minute} minutes before the start")
elif time >= 60:
    if minute < 10:
        print(f"Early\n"
              f"{hour}:0{minute} hours before the start")
    else:
        print(f"Early\n"
              f"{hour}:{minute} hours before the start")
