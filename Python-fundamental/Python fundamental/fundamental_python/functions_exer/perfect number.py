def perfect_number(num):
    lis = 0
    for i in range(1, num):
        if num % i == 0:
            lis += i
    if lis == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
result = perfect_number(number)
print(result)