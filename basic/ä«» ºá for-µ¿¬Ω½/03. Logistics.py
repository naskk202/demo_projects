packages = int(input())
small = 0
mid = 0
big = 0
for a in range(packages):
    weight = float(input())
    if weight <= 3:
        small += weight
    elif weight <= 11:
        mid += weight
    else:
        big += weight
packs = small + mid + big
small_price = small * 200
mid_price = mid * 175
big_price = big * 120
sum = (small_price + mid_price + big_price) / packs
buss = (small / packs) * 100
tir = (mid / packs) * 100
train = (big / packs) * 100
print(f"{sum:.2f}\n"
      f"{buss:.2f}%\n"
      f"{tir:.2f}%\n"
      f"{train:.2f}%")

