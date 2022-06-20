number = float(input())
importet_value = input()
result = input()
if importet_value == "m" and result == "cm":
    converted = number * 100
elif importet_value == "m" and result == "mm":
    converted = number * 1000
elif importet_value == "cm" and result == "mm":
    converted = number * 10
elif importet_value == "cm" and result == "m":
    converted = number / 100
elif importet_value == "mm" and result == "m":
    converted = number / 1000
elif importet_value == "mm" and result == "cm":
    converted = number / 10
print(f"{converted:.3f}")