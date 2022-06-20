def odd_or_even(num):
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    return odd, even


number = input()
sum = odd_or_even(number)
print(f"Odd sum = {sum[0]}, Even sum = {sum[1]}")