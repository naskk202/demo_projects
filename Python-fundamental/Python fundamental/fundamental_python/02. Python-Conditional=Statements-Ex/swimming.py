record = float(input())
meter = float(input())
time_per_meter = float(input())
resistance = (meter // 15) * 12.5
ivan_time = resistance + meter * time_per_meter
if ivan_time >= record:
    print(f"No, he failed! He was {ivan_time - record:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds."
)