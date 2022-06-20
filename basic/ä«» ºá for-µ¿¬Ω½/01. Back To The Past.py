bequest = float(input())
year = int(input())
spend = 0
for life in range(1800, year + 1):
    if life % 2 == 0:
        spend += 12000
    else:
        spend += 12000 + (50* (18 + (life - 1800)))
if bequest >= spend:
    print(f"Yes! He will live a carefree life and will have {bequest - spend:.2f} dollars left.")
else:
    print(f"He will need {spend - bequest:.2f} dollars to survive.")