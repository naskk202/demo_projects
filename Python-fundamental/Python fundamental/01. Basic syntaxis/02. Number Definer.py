number = float(input())
if number == 0:
    print("zero", end=" ")
if -1 < number < 0  or 0 < number < 1:
    print("small", end=" ")
if number > 1000000 or number < -1000000:
    print("large", end=" ")
if number < 0:
    print("negative", end=" ")
if number > 0:
    print("positive")
