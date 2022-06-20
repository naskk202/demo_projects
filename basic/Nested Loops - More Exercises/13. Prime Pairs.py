first = int(input())
second = int(input())
diff_first = int(input())
diff_second = int(input())
A = 0
B = 0
for a in range(first, first + diff_first + 1):
    for b in range(second, second + diff_second + 1):
        for counter in range(1, 91):
            if a % counter == 0:
                A += 1
            if b % counter == 0:
                B += 1
        if A < 3 and B < 3:
            print(f"{a}{b}")
        A = 0
        B = 0



first = int(input())
second = int(input())
diff_first = int(input())
diff_second = int(input())
for a in range(first, first + diff_first + 1):
    for b in range(second, second + diff_second + 1):
        if a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0and b % 2 != 0 and b % 3 != 0 and b % 5 != 0 and b % 7 != 0:
            print(f"{a}{b}")