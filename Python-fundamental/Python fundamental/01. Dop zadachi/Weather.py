degreace = float(input())
if 26 <= degreace <= 35:
    print("Hot")
elif 20.1 <= degreace <= 25.9:
    print("warm")
elif 15 <= degreace <= 20:
    print("mild")
elif 12 <= degreace <= 14.9:
    print("cool")
elif 0.5 <= degreace <= 11.9:
    print("cold")
else:
    print("unknown")