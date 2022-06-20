first_string = input().split(", ")
second_string = input().split(", ")
inn_are = []
for i in first_string:
    check = [i for word in second_string if i in word]
    if check:
        inn_are.append(check[0])
print(inn_are)
