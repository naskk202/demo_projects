from math import floor
incom = float(input())
average_success= float(input())
min_salary= float(input())
social_scholarship = min_salary * 0.35
excellent_scholarship = average_success * 25
if average_success >= 5.5 and social_scholarship <= excellent_scholarship:
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
elif average_success >= 5.5 and social_scholarship > excellent_scholarship and incom <= min_salary:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif 4.5 <= average_success and min_salary >= incom:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")







from math import floor
incom = float(input())
average_success= float(input())
min_salary= float(input())

excellent_scholarship = 0
social_scholarship = 0

if average_success >= 5.5:
    excellent_scholarship += average_success * 25
if incom < min_salary and average_success >= 4.5:
    social_scholarship = min_salary * 0.35

if social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")