num = int(input())
number = 1
for row in range (1, num + 1):
    for collum in range(1, row + 1):
        if number > num:
            break
        print(number, end = " ")
        number += 1
    print()