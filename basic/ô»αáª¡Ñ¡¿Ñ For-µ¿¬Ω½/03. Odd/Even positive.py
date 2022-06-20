import sys
num = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for a in range(1, num + 1):
    b = float(input())
    if a % 2 == 0:
        even_sum += b
        if b > even_max:
            even_max = b
        if b < even_min:
            even_min = b
    else:
        odd_sum += b
        if b > odd_max:
            odd_max = b
        if b < odd_min:
            odd_min = b
if num == 0:
    print(f"OddSum={odd_sum:.2f},\n"
          f"OddMin=No,\n"
          f"OddMax=No,\n"
          f"EvenSum={even_sum:.2f},\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")

elif even_min == sys.maxsize and even_max == -sys.maxsize:
    print(f"OddSum={odd_sum:.2f},\n"
          f"OddMin={odd_min:.2f},\n"
          f"OddMax={odd_max:.2f},\n"
          f"EvenSum={even_sum:.2f},\n"
          f"EvenMin=No,\n"
          f"EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},\n"
          f"OddMin={odd_min:.2f},\n"
          f"OddMax={odd_max:.2f},\n"
          f"EvenSum={even_sum:.2f},\n"
          f"EvenMin={even_min:.2f},\n"
          f"EvenMax={even_max:.2f}")