number_1 = int(input())
number_2 = int(input())
sign = input()
sum = 0
even_odd = 0
if sign == "+":
    sum = number_1 + number_2
elif sign == "-":
    sum = number_1 - number_2
elif sign == "*":
    sum = number_1 * number_2
elif sign == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        sum = number_1 / number_2
elif sign == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        sum = number_1 % number_2
if sum % 2 == 0:
    even_odd = "even"
elif sum %2 != 0:
    even_odd = "odd"
if sign == "+" or sign == "-" or sign == "*":
    print(f"{number_1} {sign} {number_2} = {sum} - {even_odd}")
elif sign == "/" and number_2 != 0:
    print(f"{number_1} / {number_2} = {sum:.2f}")
elif sign == "%" and number_2 != 0:
    print((f"{number_1} % {number_2} = {sum}"))