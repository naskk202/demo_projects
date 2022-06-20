def palindrome_or_no(pal):
    for num in pal:
        if int(num) < 10:
            print(True)
        else:
            for i in range(len(num) // 2):
                if num[i] == num[-i - 1]:
                    if i == len(num) // 2 - 1:
                        print(True)
                    else:
                        continue
                else:
                    print(False)
                    break
    return


palindrome = input().split(", ")
palindrome_or_no(palindrome)
