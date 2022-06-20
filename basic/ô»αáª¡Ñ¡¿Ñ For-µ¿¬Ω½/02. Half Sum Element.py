a = int(input())
max_number = 0
sum = 0
for b in range(a):
    c = int(input())
    sum += c
    if max_number < c:
        max_number = c
all = sum - max_number
if all == max_number:
    print(f"Yes\n"
            f"Sum = {all}")
else:
    print(f"No\n"
          f"Diff = {abs(all - max_number)}")