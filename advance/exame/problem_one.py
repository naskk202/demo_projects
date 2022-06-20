import sys
from io import StringIO

input1 = """105 20 30 25
120 60 11 400 10 1
"""

input2 = """30 5 21 6 0 91
15 9 5 15 8
"""

input3 = """800 1000 834
5 15 32 20 10 5
"""

sys.stdin = StringIO(input1)

from collections import deque

materials = [int(i) for i in input().split()]
magick = deque(int(i) for i in input().split())

gifts = {
    "Diamond Jewellery": 0,
    "Gemstone": 0,
    "Gold": 0,
    "Porcelain Sculpture": 0
}

first_combo = ["Gemstone", "Porcelain Sculpture"]
second_combo = ["Gold", "Diamond Jewellery"]

while materials and magick:
    cur_material = materials.pop()
    cur_magick = magick.popleft()

    cur_sum = cur_material + cur_magick

    if cur_sum < 100:
        if cur_sum % 2 == 0:
            cur_sum = cur_material * 2 + cur_magick * 3
        else:
            cur_sum = cur_sum * 2
    elif cur_sum > 499:
        cur_sum = cur_sum / 2

    if 100 <= cur_sum <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= cur_sum <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= cur_sum <= 399:
        gifts["Gold"] += 1
    elif 400 <= cur_sum <= 499:
        gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or \
        (gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(i) for i in materials)}")
if magick:
    print(f"Magic left: {', '.join(str(i) for i in magick)}")

for k, v in gifts.items():
    if v > 0:
        print(f"{k}: {v}")