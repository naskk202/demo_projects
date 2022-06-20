count = int(input())
first = 0
second = 0
third = 0
forth = 0
fifth = 0
for num in range(count):
    number = int(input())
    if number < 200:
        first += 1
    elif number < 400:
        second += 1
    elif number < 600:
        third += 1
    elif number < 800:
        forth += 1
    else:
        fifth += 1
one = (first / count) * 100
two = (second / count) * 100
three = (third / count) * 100
four = (forth / count) * 100
five = (fifth / count) * 100
print(f"{one:.2f}%\n"
      f"{two:.2f}%\n"
      f"{three:.2f}%\n"
      f"{four:.2f}%\n"
      f"{five:.2f}%")