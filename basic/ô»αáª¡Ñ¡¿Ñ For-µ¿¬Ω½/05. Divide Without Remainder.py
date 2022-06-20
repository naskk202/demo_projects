count = int(input())
second = 0
third = 0
forth = 0
for num in range(count):
    number = int(input())
    if number % 2 == 0:
        second += 1
    if number % 3 == 0:
        third += 1
    if number % 4 == 0:
        forth += 1
two = (second / count) * 100
three = (third / count) * 100
four = (forth / count) * 100
print(f"{two:.2f}%\n"
      f"{three:.2f}%\n"
      f"{four:.2f}%\n")