first_number = int(input())
second_number = int(input())
third_number = int(input())
for a in range(2, first_number + 1, + 2):
    for b in range(2, second_number + 1):
        for c in range(2, third_number + 1, +2):
            if b == 4 or b == 6 or b > 7:
                break
            else:
                print(f"{a} {b} {c}")