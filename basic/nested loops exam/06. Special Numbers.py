num = int(input())
for a in range(1111, 9999 + 1):
    str_a = str(a)
    count = 0
    b = True
    for number, digit in enumerate(str_a):
        digit = int(digit)
        if digit == 0:
            b = False
            break
        if num % digit == 0:
            count += 1
    if count == 4 and b:
        print(a, end = " ")