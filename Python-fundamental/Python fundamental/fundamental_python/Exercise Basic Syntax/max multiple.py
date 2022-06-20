divisor = int(input())
bound = int(input())
for a in range(bound, divisor -1, -1):
    if a % divisor == 0:
        print(a)
        break
