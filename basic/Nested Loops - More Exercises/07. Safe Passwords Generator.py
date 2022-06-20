a = int(input())
b = int(input())
max_pass = int(input())
password = 0
for first in range(35, 56):
    for second in range(64, 97):
        for third in range(1, a + 1):
            for forth in range(1, b + 1):
                print(f"{chr(first)}{chr(second)}{third}{forth}{chr(second)}{chr(first)}", end = "|")
                password += 1
                first += 1
                if first == 56:
                    first = 35
                second += 1
                if second == 97:
                    second = 64
                if third == a and forth == b or password == max_pass:
                    exit()