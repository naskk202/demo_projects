num = int(input())
electrons = []
for i in range(1, num):
    shell = 2 * i ** 2
    if shell <= num:
        electrons.append(shell)
        num -= shell
    else:
        if not num == 0:
            electrons.append(num)
            num = 0
            break
print(electrons)
