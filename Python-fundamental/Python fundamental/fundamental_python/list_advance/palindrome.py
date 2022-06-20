words = input().split()
palindrome = input()
palindrome_list = [i for i in words if i == "".join(reversed(i))]
print(palindrome_list)
repeat = [i for i in palindrome_list if i == palindrome]
print(f"Found palindrome {len(repeat)} times")