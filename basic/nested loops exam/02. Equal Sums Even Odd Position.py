first = int(input())
second = int(input())
for test in range(first, second +1):
    string_test = str(test)
    even = 0
    odd = 0
    for number, digit in enumerate(string_test):
        if number % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(test, end = " ")