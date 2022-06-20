projection = input()
row = int(input())
column = int(input())
if projection == "Premiere":
    print(f"{(row * column) * 12:.2f} leva")
elif projection == "Normal":
    print(f"{(row * column) * 7.5:.2f} leva")
elif projection == "Discount":
    print(f"{(row * column) * 5:.2f} leva")
