number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 > number_2 and number_1 > number_3:
    print(number_1)
elif number_1 < number_2 and number_2 > number_3:
    print(number_2)
else:
    print(number_3)




a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))