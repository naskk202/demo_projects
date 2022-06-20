town = input()
sells = float(input())
comision = 0
if town == "Sofia":
    if 0 <= sells <= 500:
        comision = sells * 0.05
    elif 500 < sells <= 1000:
        comision = sells * 0.07
    elif 1000 <  sells <= 10000:
        comision = sells * 0.08
    elif sells > 10000:
        comision = sells * 0.12
if town == "Varna":
    if 0 <= sells <= 500:
        comision = sells * 0.045
    elif 500 < sells <= 1000:
        comision = sells * 0.075
    elif 1000 <  sells <= 10000:
        comision = sells * 0.1
    elif sells > 10000:
        comision = sells * 0.13
if town == "Plovdiv":
    if 0 <= sells <= 500:
        comision = sells * 0.055
    elif 500 < sells <= 1000:
        comision = sells * 0.08
    elif 1000 <  sells <= 10000:
        comision = sells * 0.12
    elif sells > 10000:
        comision = sells * 0.145
if comision <= 0 or sells < 0:
    print("error")
else:
    print(f"{comision:.2f}")